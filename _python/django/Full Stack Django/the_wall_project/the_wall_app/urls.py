from django.urls import path     
from . import views

urlpatterns = [
    path('', views.wall),
    path('/create', views.create),
    path('/create_comment/<int:id>', views.create_comment),
    path('/delete/<int:id>', views.delete),
]