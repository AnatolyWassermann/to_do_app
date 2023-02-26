from django.shortcuts import render
from .models import ToDo
from django.http import HttpResponse

def add_todo(request):
    todo = ToDo(title='lel1', desc='tops')
    todo.save()

    return HttpResponse("product saved")
# Create your views here.
