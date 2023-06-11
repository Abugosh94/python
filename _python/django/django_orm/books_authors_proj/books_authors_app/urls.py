from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.books),
    path('add_author', views.authors),
    path('book/<str:title>', views.display),
    path('author/<int:id>', views.display_author),
    path('process', views.process),
    ]
