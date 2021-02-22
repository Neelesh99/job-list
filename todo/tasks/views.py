from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    context = {'item': item}
    if request.method == "POST":
        item.delete()
        return redirect('/')
    return render(request, 'tasks/delete.html', context)

def addApplication(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            new_application = form.save()
            user = request.user
            if UsersApplications.objects.filter(username=user.username).exists():
                userApplications: UsersApplications = UsersApplications.objects.get(username=user.username)
                privateKeys = userApplications.get_applicationPKs()
                newPKs = privateKeys['applications']
                newPKs.append(new_application.pk)
                userApplications.set_applicationPKs(newPKs)
                userApplications.save()
            else:
                return redirect('/login')
            return redirect('/applications')

    return render(request, 'applications/newApplication.html')

def deleteApplication(request, pk):
    # Delete users reference to application #
    if request.method == 'POST':
        user = request.user
        if UsersApplications.objects.filter(username=user.username).exists():
            applications: UsersApplications = UsersApplications.objects.get(username=user.username)
            keys = applications.get_applicationPKs()
            newPks: list = keys['applications']
            if int(pk) in newPks:
                newPks.remove(int(pk))
                applications.set_applicationPKs(newPks)
                applications.save()
        return redirect('/applications')
    applicationData: Application = Application.objects.get(id=pk)
    context = {'name': applicationData.name}
    return render(request, 'applications/deleteApplication.html', context)

def applicationPage(request):
    user = request.user
    applications = []
    if UsersApplications.objects.filter(username=user.username).exists():
        userApp = UsersApplications.objects.get(username=user.username)
        pks = userApp.get_applicationPKs()
        for key in pks['applications']:
            applications.append(Application.objects.get(id=key))
    context = {'applications': applications}
    return render(request, 'applications/appDashboard.html', context)
