from django.contrib import admin
from django.db.models import QuerySet
from django.urls import reverse

from .models import Book, Autor, Reader
from django.utils.html import format_html


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'autor_link')
    search_fields = ['name']
    actions = ['delete_book']

    def autor_link(self, obj):
        autor = obj.autor
        url = reverse("admin:lib_autor_changelist") + str(autor.pk)
        return format_html(f'<a href="{url}">{autor}</a>')

    autor_link.short_description = "Автор"
    @admin.action(description="Удалить книги")
    def delete_book(self, request, queryset: QuerySet):
        queryset.update(quantity=0)

    # def delete_all_books(self, request, queryset):
    #     for obj in queryset:
    #         obj.books.clear()

class AutorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class ReaderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'status', 'display_active_book']
    list_filter = ['status']
    actions = ['status_close', 'delete_book']

    @admin.action(description="Закрытый статус")
    def status_close(self, request, queryset: QuerySet):
        stat_ = queryset.update(status=False)
        self.message_user(request, f'Закрыто {stat_} читателей')

    @admin.action(description='Удалить книги из актива читателя')
    def delete_book(self, request, queryset):

        for reader in queryset.all():
            for book in reader.active_book.all():
                book = Book.objects.get(pk=book.pk)
                book.quantity += 1
                book.save()
                reader.active_book.remove(book)


admin.site.register(Book, BookAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Reader, ReaderAdmin)
