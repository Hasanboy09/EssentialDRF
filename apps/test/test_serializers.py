import pytest
from apps.test.test_fixtures import *

from apps.serializers import BookSerializer


@pytest.mark.django_db
def test_book_deserializer():
    book = {
        "name": "Choliqushi",
    }
    obj = BookSerializer(data=book)
    assert obj.is_valid()
    assert obj.validated_data['name'] == 'Choliqushi'


@pytest.mark.django_db
def test_book_serializer(book):
    book = Book.objects.first()
    data = BookSerializer(book).data
    assert isinstance(data, dict)
    assert data['id'] == 1
    assert data['name'] == 'Oq kema'
