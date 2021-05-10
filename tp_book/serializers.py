from rest_framework import serializers
from tp_book.models import Book


class BookSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
