from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from lib.models import Autor, Book, Reader
from lib.serializers import AutorSerializer, BookSerializer, ReaderSerializer

from .permissions import PermissionPolicyMixin, PermissionReader
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


# class AutorViewSet(ModelViewSet):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializer
#
#
# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class ReaderViewSet(ModelViewSet):
#     queryset = Reader.objects.all()
#     serializer_class = ReaderSerializer

class AutorViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'retrieve': [IsAdminUser]
    }

#
class BookViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'retrieve': [IsAdminUser]
    }


class ReaderViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes_per_method = {
        'list': [IsAdminUser, IsAuthenticated],
        'create': [AllowAny],
        'update': [PermissionReader],
        'destroy': [PermissionReader],
        'retrieve': [PermissionReader]
    }
