from django.urls import path
from .views import todo_list_view, todo_detail_view, todo_create_view, todo_delete_view

urlpatterns = [
    path('create/', todo_create_view, name='create'), 
    path('delete/<slug:slug>/', todo_delete_view, name='delete' ),
    path('', todo_list_view, name='home'),   
    path('<slug:slug>/', todo_detail_view, name='detail'), 
]