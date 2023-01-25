from django.shortcuts import render
from .models import *
from .forms import *

def todo_list(request) :
    todos = Todo.objects.all()
    context = {
        "todos" : todos
    }

    return render(request,'list.html',context)