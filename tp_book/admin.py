from django.contrib import admin
from tp_book.models import Book


class AdminMode(admin.ModelAdmin):
    list_display = [
        'name',
        'store_name',
        'favorite',
        'create_date'
    ]
    search_fields = [
        'name',
        'store_name'
    ]


# Register your models here.
admin.site.register(Book, AdminMode)
