from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('courses/destroy/<int:id>', views.confirm),
    path('courses/destroy/<int:id>/delete', views.delete),
    path('courses/<int:id>', views.course),
    path('courses/<int:id>/add_comment', views.add_comment),
    ]
