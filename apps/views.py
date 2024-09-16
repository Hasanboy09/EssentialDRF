import random

from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.models import Book, Unit, Test, User
from apps.serializers import BookSerializer, RegisterUserSerializer, UnitSerializer, TestSerializer
from apps.tasks import send_email


# @extend_schema(tags=['user'])
# class CreateUserModelViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = RegisterUserSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)

@extend_schema(tags=['user'])
class UserCreateView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


@extend_schema(tags=['verification'])
class SendEmail(APIView):
    permission_classes = permissions.AllowAny,

    def post(self, request):  # noqa
        receiver_email = request.POST['email']
        generate_code = random.randint(10 ** 5, 10 ** 6)
        send_email("Verification Code", f"code: {generate_code}", receiver_email)
        return Response({'code': f"generate_code"}, status=HTTP_200_OK)


@extend_schema(tags=['book'])
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # parser_classes = (MultiPartParser, FormParser)

    # def create(self, request):
    #     file_uploaded = request.FILES.get('file_uploaded')
    #     content_type = file_uploaded.content_type
    #     response = "POST API and you have uploaded a {} file".format(content_type)
    #     return Response(response)


@extend_schema(tags=['book'])
class BookCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@extend_schema(tags=['unit'])
class UnitCreateAPIView(CreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    parser_classes = [FileUploadParser]


@extend_schema(tags=['test'])
class TestModelViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    parser_classes = [FileUploadParser]
