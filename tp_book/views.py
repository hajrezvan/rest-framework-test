from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from tp_book.models import Book
from tp_book.serializers import BookSerializerModel


# Create your views here.
class GetAllDate(APIView):
    def get(self, request):
        query = Book.objects.all().order_by('-create_date')
        serializer = BookSerializerModel(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetFavData(APIView):
    def get(self, request):
        query = Book.objects.filter(favorite=True)
        serializer = BookSerializerModel(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateFavData(APIView):
    def put(self, request, primary_key):
        query = Book.objects.get(pk=primary_key)
        serializer = BookSerializerModel(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostData(APIView):
    def post(self, request):
        serializer = BookSerializerModel(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchData(APIView):
    def get(self, request):
        search = request.GET['name']
        query = Book.objects.filter(store_name__contains=search)
        serializer = BookSerializerModel(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteData(APIView):
    def delete(self, request, primary_key):
        query = Book.objects.filter(pk=primary_key)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
