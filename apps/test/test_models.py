import pytest

from apps.models import Book
from apps.test.test_fixtures import *

@pytest.mark.django_db  #modelnitekshirish
def test_book_model(book):
    book = Book.objects.get(name='Tungi hikoya')
    assert book.name == 'Tungi hikoya'
    assert book.id == 2
