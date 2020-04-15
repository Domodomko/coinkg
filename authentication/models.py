from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings

from . user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    name = models.CharField(verbose_name='Name', max_length=255)
    surname = models.CharField(verbose_name='Surname', max_length=255)
    patronymic = models.CharField(verbose_name='Patronymic', max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(verbose_name='Phone', max_length=255)
    address = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    job = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'patronymic', 'phone', 'address']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    class Meta:
        verbose_name = 'пользователи'
        verbose_name_plural = 'Пользователи'
