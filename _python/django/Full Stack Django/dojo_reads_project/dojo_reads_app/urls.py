from django.urls import path     
from . import views

urlpatterns = [
    path('', views.books),
    path('/add_book', views.add_book),
    path('/process', views.process),
    ]