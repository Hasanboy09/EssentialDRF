from http import HTTPStatus
from os.path import join

import pytest
from rest_framework.reverse import reverse

from apps.models import Book
from apps.test.test_fixtures import *
from root.settings import BASE_DIR


@pytest.mark.django_db
def test_book_list(client, book):
    path = reverse('book-create-list')
    response = client.get(path)
    assert len(response.data) == 4
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_book_create(client, book):
    path = reverse('book-create-list')
    response = client.post(path, data={'name': 'Jaloliddin'})
    book = Book.objects.count()
    assert response.status_code == HTTPStatus.CREATED
    assert book == 5


import os
from django.conf import settings


@pytest.mark.django_db
def test_book_create_image(client, book):
    path = reverse('book-create-list')
    image_path = os.path.join(settings.BASE_DIR, "images.jpeg")
    with open(image_path, 'rb') as fp:
        data = {
            "name": "Jaloliddin",
            "image": fp
        }
        response = client.post(path, data=data, content_type='multipart/form-data' , format='multipart')
    print(response.status_code)
    print(response.data)

