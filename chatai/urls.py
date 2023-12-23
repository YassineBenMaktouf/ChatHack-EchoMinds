# analysis_app/urls.py

from django.urls import path
from .views import chatai, download, chat

urlpatterns = [
    path('', chatai, name='chatai'),
    path('download/<str:filename>/', download, name='download'),
    path('chat/', chat, name='chat'),
]
