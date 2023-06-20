# todo/todo_api/urls.py : API urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('prices', CandlestickByStock.as_view()),
]