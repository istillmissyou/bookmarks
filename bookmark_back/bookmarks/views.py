import requests

from bs4 import BeautifulSoup
from collections_bm.models import Collection
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Bookmark
from .serializers import (AddToCollectionSerializer, BookmarkSerializer,
                          CreateBookmarkSerializer, ResponseBookmarkSerializer)

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}


def get_object_or_error(model, model_id, error_message):
    try:
        return model.objects.get(id=model_id)
    except model.DoesNotExist:
        return Response({'error': True, 'message': error_message}, status=status.HTTP_200_OK)


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    http_method_names = ['post', 'delete']

    @staticmethod
    def extract_og_data(url):
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')

        find_content = lambda prop: soup.find("meta", property=prop)["content"] if soup.find("meta", property=prop) else None

        return {
            "title": find_content("og:title") or soup.title.string,
            "description": find_content("og:description") or find_content("description"),
            "image": find_content("og:image"),
            "link_type": find_content("og:type") or 'website'
        }

    @swagger_auto_schema(request_body=CreateBookmarkSerializer,
        responses={201: ResponseBookmarkSerializer(), 400: "Bad Request"})
    def create(self, request):
        """ Создать закладку. """
        serializer = CreateBookmarkSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        url = serializer.validated_data['url']

        bookmark = Bookmark.objects.filter(url=url, user=user).first()
        if bookmark:
            return Response({'error': False, 'message': 'OK', 'payload': BookmarkSerializer(bookmark).data}, status=status.HTTP_200_OK)
        bookmark = Bookmark.objects.filter(url=url).first()
        if bookmark:
            bookmark = Bookmark.objects.create(url=url, title=bookmark.title, description=bookmark.description, link_type=bookmark.link_type, og_image=bookmark.og_image, user=user)
            return Response({'error': False, 'message': 'OK', 'payload': BookmarkSerializer(bookmark).data}, status=status.HTTP_200_OK)
        og_data = self.extract_og_data(url)

        bookmark = Bookmark.objects.create(url=url,
            title=og_data["title"], description=og_data["description"],
            link_type=og_data["link_type"], og_image=og_data["image"], user=user)

        return Response({'error': False, 'message': 'OK', 'payload': BookmarkSerializer(bookmark).data}, status=status.HTTP_200_OK)


    @action(detail=False, methods=['post'], url_path='add_to_collection', serializer_class=AddToCollectionSerializer)
    def add_to_collection(self, request, pk=None):
        """ Добавить закладку в коллекцию. """

        bookmark_id = request.data.get('bookmark_id')
        collection_id = request.data.get('collection_id')

        bookmark = get_object_or_error(Bookmark, bookmark_id, 'Bookmark not found')
        if isinstance(bookmark, Response):
            return bookmark

        collection = get_object_or_error(Collection, collection_id, 'Collection not found')
        if isinstance(collection, Response):
            return collection

        if collection.bookmarks.filter(id=bookmark_id).exists():
            return Response({'error': True, 'message': 'Bookmark already in this collection'}, status=status.HTTP_200_OK)

        collection.bookmarks.add(bookmark)
        return Response({'error': False, 'message': 'Bookmark added to collection'}, status=status.HTTP_200_OK)
