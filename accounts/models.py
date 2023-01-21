from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        username = self.normalize_email(username)

        user = self.model(
            username=username,
            **extra_fields
        )

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(username=username, password=password, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(max_length=80, unique=True)
    nickname = models.CharField(max_length=45)
    photo = models.ImageField(upload_to='media/user_photo')

    objects = CustomUserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["photo", "nickname"]

    def __str__(self):
        return self.username


