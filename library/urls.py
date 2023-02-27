"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework import viewsets

from lib import views
from lib.views import BookViewSet, AutorViewSet, ReaderViewSet
router = routers.SimpleRouter()
router.register(r'book', views.BookViewSet)
router.register(r'autor', views.AutorViewSet)
router.register(r'reader', views.ReaderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

]
urlpatterns += router.urls
# from lib.views import ReaderListView, AutorListView, BookListView
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("book/", BookListView.as_view()),
#     path("autor/", AutorListView.as_view()),
#     path("reader/", ReaderListView.as_view())
# ]
