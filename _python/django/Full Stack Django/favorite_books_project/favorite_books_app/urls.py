from django.urls import path     
from . import views

urlpatterns = [
    path('', views.books),
    path('/create', views.create),
    path('/fav/<int:id>', views.add_favorite),
    path('/<int:id>', views.view),
    path('/favs', views.view_favs),
    path('/unfavorite/<int:id>', views.remove_favorite),
    path('/delete/<int:id>', views.delete),
]