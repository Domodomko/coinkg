from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

from authentication.models import User


CONTACT_TYPES = (
    ('PHONE', 'Телефон'),
    ('FACEBOOK', 'Facebook'),
    ('EMAIL', 'E-mail'),
    ('WHATSAPP', 'Whatsapp'),
)

PRODUCT_TYPES = (
    ('Потребительский кредит', 'Потребительский кредит'),
    ('Агрокредит', 'Агрокредит'),
    ('Автокредит', 'Автокредит'),
    ('Кредит для развития бизнеса', 'Кредит для развития бизнеса'),
    ('Ипотека', 'Ипотека'),
)

CURRENCY_TYPES = (
    ('СОМ', 'Сом'),
    ('USD', 'USD'),
)


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = RichTextField(verbose_name='Содержание')
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    image = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'


class SuccessStory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = RichTextField(verbose_name='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-title',)
        verbose_name = 'информацию о истории успеха'
        verbose_name_plural = 'История успеха'


class AboutUs(models.Model):
    content = RichTextField(verbose_name="Текст")

    def __str__(self):
        return "Текст о нас"

    class Meta:
        verbose_name = 'информацию о нас'
        verbose_name_plural = 'О нас'


class Contact(models.Model):
    # TO-DO: Разобраться с полями
    type = models.CharField(choices=CONTACT_TYPES, max_length=30, verbose_name='Тип контакта')
    value = models.CharField(max_length=100, default='value', verbose_name='Значение')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'Контакты'


class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(default='')
    content = models.TextField(verbose_name='Текст')
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'обратную связь'
        verbose_name_plural = 'Обратная связь'


class Credit(models.Model):
    user = models.ForeignKey('authentication.User', related_name='credits', on_delete=models.PROTECT)
    sum = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Сумма')
    time = models.DateField(verbose_name='На какое время')
    passport = models.FileField(verbose_name='Скан пасспорта')
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    product = models.CharField(choices=PRODUCT_TYPES, max_length=100, verbose_name='Продукт')
    currency = models.CharField(choices=CURRENCY_TYPES, max_length=30, verbose_name='Валюта')
    other_credits = models.BooleanField(default=False, verbose_name="Есть ли другие кредиты?")
    verify = models.BooleanField(default=False, verbose_name="Одобрен")

    def __str__(self):
        return '{}'.format(self.user)

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'заявку на кредит'
        verbose_name_plural = 'Заявка на кредит'


class CreditsInfo(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'информацию о кредитах'
        verbose_name_plural = 'Информация о кредитах'

