# Foodgram
Project address http://51.250.15.126
# Description
On this service, users can publish recipes, subscribe to other users' posts, add their favorite recipes to the "Favorites" list, and before going to the store download a summary list of products needed to prepare one or more selected dishes.

# Technologies
Python 3.9
Django 3.2
Django REST Framework 3.12
Djoser 2.1.0
Docker
# Quick start
Go to the directory 'infra' and run in command line:
```sh 
docker-compose up -d
```
Run in command line:
```sh 
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py collectstatic
```
To load data:
```sh
docker-compose exec app python manage.py load_data
```
# Authors
Vitalii Tsoma - Backend, DevOps part
Yandex Praktikum - Frontend part

