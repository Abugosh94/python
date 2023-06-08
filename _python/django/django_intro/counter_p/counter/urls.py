from django.urls import path     
from . import views
urlpatterns = [
    path('',views.index),
    path('destroy',views.destroysession),
    path('addtwo',views.addtwo),
    path('addcustom',views.addcustom),
    ]
