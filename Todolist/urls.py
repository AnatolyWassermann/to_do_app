from django.urls import path
 

from .views import todo_list_view, todo_detail_view, create_todo

urlpatterns = [
    path('create/', create_todo, name='create'),
    path('<slug:slug>/', todo_detail_view, name='detail'),
    path('', todo_list_view, name='home'),
    
]