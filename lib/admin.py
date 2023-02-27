from django.contrib import admin
from django.db.models import QuerySet

from .models import Book, Autor, Reader


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')
    search_fields = ['name']

    # def autor_link(self, obj):
    #     autor = obj.autor
    #     url = reverse("admin:library_autor_changelist") + str(autor.pk)
    #     return format_html(f' <a href')


class AutorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class ReaderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'status']
    list_filter = ['active_book']
    action = ['status_close']

    @admin.action(description="Закрытый статус")
    def status_close(self, request, queryset: QuerySet):
        queryset.update(status=False)
        # self.message_user()


admin.site.register(Book, BookAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Reader, ReaderAdmin)
