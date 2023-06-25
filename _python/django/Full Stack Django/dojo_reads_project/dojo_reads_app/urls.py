from django.urls import path     
from . import views

urlpatterns = [
    path('', views.books),
    path('/add_book', views.add_book),
    path('/process', views.process),
    path('/<int:id>', views.view_book),
    path('/<int:id>/add_review', views.add_review),
    ]