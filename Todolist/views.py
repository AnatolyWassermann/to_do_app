from django.shortcuts import render
from .models import ToDo
from django.http import HttpResponse

def add_todo(request):
    todo = ToDo(title='lel1', desc='tops', completed=True)
    todo.save()
    

    return HttpResponse(f"{todo} {todo.desc}, {todo.completed} {todo.created}product saved")
# Create your views here.
