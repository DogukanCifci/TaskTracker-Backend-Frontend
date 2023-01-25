from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_list,name="index"),
    # path('add/', todo_add, name="todo_app")
]
