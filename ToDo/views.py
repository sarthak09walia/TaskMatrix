from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import ToDo_Create
from .models import Todo
from django.contrib.auth.decorators import login_required
 

def Create_ToDo(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ToDo_Create(request.POST)
        # Handle form submission and validation for POST requests
        if form.is_valid():
            todo=Todo.objects.create(title=form.cleaned_data['title'], description=form.cleaned_data['description'],status=form.cleaned_data['status'],ToDO_User=request.user,due_date=form.cleaned_data['due_date'])
            messages.success(request, f'Task created successfully {todo.title}!')
            return redirect('Tasks')
        else:
            return render(request, 'ToDo/Create_ToDo.html', {'form': form})
    else:
        form = ToDo_Create()
    
    return render(request, 'ToDo/Create_ToDo.html', {'form': form})


@login_required
def all_task(request):
    if request.method == 'GET' and request.user.is_authenticated:
        ToDo_list = Todo.objects.filter(ToDO_User=request.user)
        return render(request, 'ToDo/post.html',{'ToDo_list':ToDo_list})


@login_required
def view_task(request, id):
    if request.method == 'GET' and request.user.is_authenticated:
        task = get_object_or_404(Todo, id=id)
        return render(request, 'ToDo/View_Task.html', {'task': task})
    
@login_required
def edit_task(request, id):
    task = get_object_or_404(Todo, id=id)

    if request.method == 'POST':
        form = ToDo_Create(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task', id=id)  # Redirect to the task detail view
    else:
        form = ToDo_Create(instance=task)

    return render(request, 'ToDo/edit_task.html', {'form': form, 'task': task})


@login_required
def delete_task(request, id):
    if request.method =='POST':
        task = get_object_or_404(Todo, id=id)
        messages.success(request, f'Task deleted successfully {task.title}!')
        task.delete()
        return redirect('Tasks')
    elif request.method == 'GET':
        task = get_object_or_404(Todo, id=id)
        return render(request, 'ToDo/Delete_Task.html', {'task': task})


