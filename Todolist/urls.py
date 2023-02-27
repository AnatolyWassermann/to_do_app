from django.urls import path
 

from .views import todo_list_view, todo_detail_view

urlpatterns = [
    path('', todo_list_view, name='home'),
    path('<str:slug>/', todo_detail_view, name='detail'),
]