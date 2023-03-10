from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Autor(models.Model):
    # - имя
    # - фамилия
    # - фото
    # - дата создания
    # - дата редактирования
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    foto = models.ImageField(upload_to='foto/', blank=True, verbose_name='фото')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата редактирования', auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    # название
    # описание
    # кол - во станиц
    # автор
    # кол-во в библеотеке
    # дата создания
    # дата редактирования
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание', max_length=255)
    number_of_page = models.PositiveIntegerField(verbose_name='количество страниц')
    autor = models.ForeignKey(Autor,  blank=False, on_delete=models.CASCADE, verbose_name='автор')
    quantity = models.PositiveIntegerField(verbose_name='количество')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата редактирования', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Reader(AbstractUser):
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    phone = models.BigIntegerField(verbose_name='номер телефона', null=True) #unique=True
    status = models.BooleanField(default=True)
    active_book = models.ManyToManyField(Book, blank=True, verbose_name='активные книги')
    updated = models.DateTimeField(verbose_name='дата редактирования', auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def display_active_book(self):
        return ', '.join([active_book.name for active_book in self.active_book.all()])

    display_active_book.short_description = 'Активные книги'

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'
# class Reader(models.Model):
#     # - имя
#     # - фамилия
#     # номер телефона
#     # статус читателя по умолчанию активный
#     # активные книги
#     # - дата создания
#     # - дата редактирования
#     first_name = models.CharField(verbose_name='Имя', max_length=255)
#     last_name = models.CharField(verbose_name='Фамилия', max_length=255)
#     number = models.BigIntegerField(verbose_name='номер телефона', unique=True)
#     status = models.BooleanField(default=True)
#     active_book = models.ManyToManyField(Book, blank=True, verbose_name='активные книги')
#     created = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
#     updated = models.DateTimeField(verbose_name='дата редактирования', auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def display_active_book(self):
#         return ', '.join([active_book.name for active_book in self.active_book.all()])
#
#     display_active_book.short_description = 'Активные книги'
#
#     class Meta:
#         verbose_name = 'Читатель'
#         verbose_name_plural = 'Читатели'
#
