# bookmarks
Django приложение с REST API c системой закладок и коллекций. Отправьте ссылку на сайт, который хотите сохранить и в базу добавится вся нужная инофрмация о сайте. Создавайте и пополняйте свои коллекции.

## Стек технологий
Python 3.10.6, Django 3.4.1, Django REST Framework 3.14.0, PostgreSQL, Docker, Docker Compose

## Установка
Для запуска, создайте файл `.env` в главной директории рядом с файлом "docker-compose.yml":
```
DB_USER=db_user
DB_PASS=db_pass
DB_NAME=bookmarks
DB_HOST=db
DB_PORT=5432
SECRET_KEY='django-insecure-0wb8lpaz0!&2uaxkl3)vq(h3qu*y$!$1#zkb$0*xneq94upd#g'
```

#### Установка Docker и docker compose
Для запуска проекта вам потребуется установить Docker и docker-compose.

Установку на операционных системах вы можете прочитать в [документации](https://docs.docker.com/engine/install/) и [про установку docker-compose](https://docs.docker.com/compose/install/).

## Запустить проект
Запустите docker compose:
```bash
docker compose up --build -d
```

## Аутентификация
Получаем токен и при следующих запросах отправляем его в хедере Authorization со значением Token <токен>

## Документация к API
Чтобы открыть документацию локально, запустите сервер и перейдите по ссылке:
[http://127.0.0.1/swagger/](http://127.0.0.1/swagger/)
[http://127.0.0.1/redoc/](http://127.0.0.1/redoc/)

## Автор
Штунь Данил
