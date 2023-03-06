# Generated by Django 4.1.6 on 2023-03-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=255, verbose_name="Фамилия")),
                (
                    "foto",
                    models.ImageField(
                        blank=True, upload_to="foto/", verbose_name="фото"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="дата редактирования"
                    ),
                ),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "description",
                    models.TextField(max_length=255, verbose_name="Описание"),
                ),
                (
                    "number_of_page",
                    models.PositiveIntegerField(verbose_name="количество страниц"),
                ),
                ("quantity", models.PositiveIntegerField(verbose_name="количество")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="дата редактирования"
                    ),
                ),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lib.autor",
                        verbose_name="автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
        migrations.CreateModel(
            name="Reader",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=255, verbose_name="Фамилия")),
                (
                    "number",
                    models.BigIntegerField(unique=True, verbose_name="номер телефона"),
                ),
                ("status", models.BooleanField(default=True)),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата редактирования"
                    ),
                ),
                (
                    "active_book",
                    models.ManyToManyField(
                        blank=True, to="lib.book", verbose_name="активные книги"
                    ),
                ),
            ],
            options={
                "verbose_name": "Читатель",
                "verbose_name_plural": "Читатели",
            },
        ),
    ]
