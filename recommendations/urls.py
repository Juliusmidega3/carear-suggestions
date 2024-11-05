# recommendations/urls.py

from django.urls import path
from . import views

app_name = 'recommendations'  # Ensure this is defined

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.get_recommendations, name='get_recommendations'),
]
