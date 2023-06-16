from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout),
    path('checkout_page', views.checkout_page),
    path('order/<int:id>', views.order),
    path('clear', views.clear),
]
