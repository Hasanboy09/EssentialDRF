from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, FileField, ForeignKey, CASCADE, SlugField, DateTimeField, \
    EmailField
from django.utils.text import slugify


# Create your models here.


# class CustomUserManager(BaseUserManager):
#     def create_user(self, phone_number, password=None, **extra_fields):
#         if not phone_number:
#             raise ValueError('The Phone Number field must be set')
#         user = self.model(phone_number=phone_number, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, phone_number, password, **extra_fields):
#         user = self.create_user(phone_number, password, **extra_fields)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user
#
#
# class User(AbstractUser):
#     class Role(TextChoices):
#         ADMIN = "admin", 'Admin'
#         USER = "user", 'User'
#
#     username = None
#     email = EmailField(unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()
#     role = CharField(max_length=50, choices=Role.choices, default=Role.USER)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Phone Number field must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    email = EmailField(unique=True)


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while self.__class__.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)


class Book(SlugBaseModel):
    name = CharField(max_length=100)
    image = ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Unit(SlugBaseModel):
    name = CharField(max_length=100)
    file = FileField(upload_to='images/')
    book = ForeignKey('apps.Book', CASCADE, related_name='units')

    def __str__(self):
        return self.name


class Test(SlugBaseModel):
    uz_language = CharField(max_length=100)
    en_language = CharField(max_length=100)
    answer = CharField(max_length=100)
    unit = ForeignKey('apps.Unit', on_delete=CASCADE, related_name='tests')
    audio = FileField(upload_to='audios/')
