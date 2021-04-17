from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('powers', views.powers),
    path('add_power', views.add_power)
]