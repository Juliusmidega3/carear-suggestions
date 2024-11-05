# recommendations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.get_recommendations, name='get_recommendations'),
]
