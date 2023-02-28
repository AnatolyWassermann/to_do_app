from django.urls import path
 

from .views import todo_list_view, todo_update_view, todo_create_view

urlpatterns = [
    path('create/', todo_create_view, name='create'),
    path('<slug:slug>/', todo_update_view, name='update'),
    path('', todo_list_view, name='home'),
    
]