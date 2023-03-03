from django.shortcuts import render, redirect
from .models import ToDo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    
    return render(request, 'signup.html', context)




class UserLogin(LoginView):
    template_name = 'login.html'

def todo_list_view(request):
    
    queryset = ToDo.objects.all()
    context = {'obj': queryset}
    return render(request, 'home.html', context)

@login_required
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