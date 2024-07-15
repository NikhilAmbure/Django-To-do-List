from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = task.objects.all()

    form = taskForm()

    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'list.html', context)

def updateTask(request, pk):

    Task = task.objects.get(id=pk)

    # Instance of Task that we got from id
    form = taskForm(instance=Task)
    
    if request.method == 'POST':
        form = taskForm(request.POST, instance=Task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'update_task.html', context)


def delete(request, pk):
    item = task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'delete.html', context)