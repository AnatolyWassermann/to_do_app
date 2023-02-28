from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm

def todo_list_view(request):
    
    queryset = ToDo.objects.all()

    context = {'obj': queryset}

    return render(request, 'home.html', context)

def todo_detail_view(request, slug):

    queryset = ToDo.objects.get(slug=slug)

    context = {'obj': queryset}

    return render(request, 'detail.html', context)
   

def create_todo(request):

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ToDoForm()
    
    return render(request, 'create_todo.html', {'form':form})