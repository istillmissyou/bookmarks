from rest_framework import viewsets

from .models import Collection
from .serializers import CollectionSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    http_method_names = ['post', 'delete', 'head', 'options', 'patch']
