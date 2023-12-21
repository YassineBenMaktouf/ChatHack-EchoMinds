from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    # Add more URL patterns here
]
