from django.db import models
from django.shortcuts import render, redirect
from .models import Todo

def index (request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            title=request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    return render(request, 'index.html', {'todos': todo})

# Create your views here.
