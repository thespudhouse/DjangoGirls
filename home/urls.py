from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('youtube/', views.home_youtube, name='home_youtube'),
    path('spaceinvaders/', views.home_spaceinvaders, name='home_spaceinvaders'),
]
