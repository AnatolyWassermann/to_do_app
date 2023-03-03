from django.urls import path
from .views import todo_list_view, todo_update_view, todo_create_view, todo_delete_view, UserLogin, signup_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('create/', todo_create_view, name='create'), 
    path('delete/<slug:slug>/', todo_delete_view, name='delete' ),
    path('accounts/login/', UserLogin.as_view(), name='login'),
    path('', todo_list_view, name='home'),   
    path('<slug:slug>/', todo_update_view, name='update'), 
]