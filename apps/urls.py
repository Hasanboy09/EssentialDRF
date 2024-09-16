from django.urls import path
from pkg_resources.extern import names

from apps.views import TestModelViewSet, UserCreateView, SendEmail, \
    BookRetrieveUpdateDestroyAPIView, UnitCreateAPIView, BookCreateAPIView

urlpatterns = [
    path('book', BookCreateAPIView.as_view() , name="book-create-list"),
    path('book/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view() , name="book-delete-update-retrieve"),

    path('unit' , UnitCreateAPIView.as_view() , name="unit-create" ),
    path('test', TestModelViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),

    path('register', UserCreateView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('send-email', SendEmail.as_view()),

]
