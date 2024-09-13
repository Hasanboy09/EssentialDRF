from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from apps.models import User, Book, Unit, Test


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'email', 'password',
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        attrs['password'] = make_password(password)
        return attrs


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        exclude = 'slug',


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
