from django.urls import path
from . import views

urlpatterns = [
    path('create_todo/', views.Create_ToDo, name='Create_ToDo'),
    path('tasks/', views.all_task, name='Tasks'),
    path('task/<int:id>/', views.view_task, name='task'),
    path('task/edit/<int:id>/', views.edit_task, name='edit_task'),
]
