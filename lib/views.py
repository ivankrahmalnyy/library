from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from lib.models import Autor, Book, Reader
from lib.serializers import AutorSerializer, BookSerializer, ReaderSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer




# from django.shortcuts import render
# from django.views import View
# from rest_framework import viewsets
# from rest_framework.generics import ListAPIView
#
# from lib.models import Autor, Book, Reader
# from lib.serializers.autor_serializers import AutorSerializer
# from lib.serializers.book_serializers import BookSerializer
# from lib.serializers.reader_serializers import ReaderSerializer
#
#
# class AutorListView(ListAPIView):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializer
#
#
# class BookListView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class ReaderListView(ListAPIView):
#     queryset = Reader.objects.all()
#     serializer_class = ReaderSerializer
