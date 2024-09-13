from django.urls import path

from apps.views import BookModelViewSet, UnitModelViewSet, TestModelViewSet, UserCreateView, SendEmail

urlpatterns = [
    path('book', BookModelViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('unit',  UnitModelViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('test',  TestModelViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),

    path('register', UserCreateView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('send-email', SendEmail.as_view()),

]
