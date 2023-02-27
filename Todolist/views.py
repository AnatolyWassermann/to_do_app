from django.shortcuts import render
from .models import ToDo
from django.http import HttpResponse

def todo_list_view(request):
    
    queryset = ToDo.objects.all()

    context = {'obj': queryset}

    return render(request, 'home.html', context)

def todo_detail_view(request, slug):

    queryset = ToDo.objects.get(slug=slug)

    context = {'obj': queryset}

    return render(request, 'detail.html', context)
   

