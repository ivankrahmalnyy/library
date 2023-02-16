from django.contrib import admin

from .models import Book, Autor, Reader
admin.site.register(Book)
admin.site.register(Autor)
admin.site.register(Reader)
