import pytest

from apps.models import Book


@pytest.fixture
def book():
    Book.objects.create(name='Oq kema')
    Book.objects.create(name='Tungi hikoya')
    Book.objects.create(name='Temur')
    Book.objects.create(name="Chayonlar so`qmog`i")

