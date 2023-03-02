from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm


def todo_list_view(request):
    
    queryset = ToDo.objects.all()
    context = {'obj': queryset}
    return render(request, 'home.html', context)

def todo_update_view(request, slug):

    todo = ToDo.objects.get(slug=slug)
    
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.desc = request.POST['desc']
        completed = request.POST.get('completed', False)
        # if completed is not None:
        #     completed = True 
        # else:
        #     completed = False        
        todo.completed = bool(completed)
        todo.save()
        return redirect('home')
    context = {
        'obj' : todo
    }

    return render(request, 'detail.html', context)
   

def todo_create_view(request):

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ToDoForm()
    
    return render(request, 'create_todo.html', {'form':form})

def todo_delete_view(request, slug):

    todo = ToDo.objects.get(slug=slug)

    if request.method == 'POST':
        todo.delete()
        return redirect('home')
        
    context = {
        'obj': todo
    }

    return render(request, 'delete.html', context)