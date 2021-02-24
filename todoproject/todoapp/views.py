from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UpdateForm


def listTask(request):
    query = Task.objects.order_by('complete', 'due')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'list_task.html', {'tasks': query,
                                              'form': form, })


def UpdateTask(request, pk):
    query = Task.objects.get(id=pk)
    form = UpdateForm(instance=query)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'update_task.html', {'form': form, })


def deleteTask(request, pk):
    query = Task.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('/')

    return render(request, 'delete_task.html', {'item': query})
