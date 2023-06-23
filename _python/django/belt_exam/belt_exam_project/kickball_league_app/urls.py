from django.urls import path     
from . import views

urlpatterns = [
    path('', views.teams),
    path('/new', views.new_team),
    path('/addteam', views.add_team),
    path('/<int:id>', views.view_team),
    path('/<int:id>/addplayer', views.add_player),
    path('/<int:id>/edit', views.edit_team),
    path('/<int:id>/update', views.update_team),
    path('/<int:id>/delete', views.delete_team),
    ]