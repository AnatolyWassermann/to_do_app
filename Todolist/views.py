from django.shortcuts import render, redirect
from .models import ToDo
from django.contrib.auth.decorators import login_required






def todo_list_view(request):
    
    queryset = ToDo.objects.all()
    context = {'obj': queryset}
    return render(request, 'home.html', context)

@login_required
def todo_detail_view(request, slug):

    todo = ToDo.objects.get(slug=slug)
    
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.desc = request.POST['desc']
        completed = request.POST.get('completed', False)
        # if completed is not None:
        #     completed = True 
        # else:
        #     completed = False   
        ''' mongodb expects bool type input '''     
        todo.completed = bool(completed)
        todo.save()
        return redirect('home')
    context = {
        'obj' : todo
    }

    return render(request, 'detail.html', context)
   
@login_required
def todo_create_view(request):

    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        user = request.user.pk
        ToDo.objects.create(title=title, desc=desc, user=user)
        return redirect('home')
    
    return render(request, 'create_todo.html')

@login_required
def todo_delete_view(request, slug):

    todo = ToDo.objects.get(slug=slug)

    if request.method == 'POST':
        todo.delete()
        return redirect('home')
        
    context = {
        'obj': todo
    }

    return render(request, 'delete.html', context)

