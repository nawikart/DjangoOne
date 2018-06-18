from django.shortcuts import render, redirect
from django.contrib import messages
from . import models as m

# Create your views here.

def index(request):
    if request.method == 'POST':
        try:
            project = m.Project()
            project.title = request.POST['html_title']
            project.user_id = request.session['user_id']
            project.save()
        except:
            messages.error(request, 'invalid input')


    context = {
        'all_projects': m.Project.objects.filter(user_id=request.session['user_id'])
    }    
    return render(request, 'project_manager/index.html', context = context)


def edit_project(request, project_id):
    
    project = m.Project.objects.get(id=project_id)

    if request.method == 'POST':
        project.title = request.POST['html_title']
        project.save()
        return redirect('project_manager:index')

    context = {
        'project': project
    } 

    return render(request, 'project_manager/edit_project.html', context = context)


def delete_project(request, project_id):
    project = m.Project.objects.get(id=project_id)
    project.delete()
    return redirect('project_manager:index')


def tasks(request, project_id):
    if request.method == 'POST':
        try:
            task = m.Task()
            task.description = request.POST['html_description']
            task.project_id = project_id
            task.save()
        except:
            messages.error(request, 'invalid input')

    context = {
        'all_tasks': m.Task.objects.filter(project_id=project_id),
        'project': m.Project.objects.get(id=project_id)
    }

    return render(request, 'project_manager/tasks.html', context = context)


def edit_task(request, task_id):
    task = m.Task.objects.get(id=task_id)

    if request.method == 'POST':
        task = m.Task.objects.get(id=task_id)
        task.description = request.POST['html_description']
        task.save()
        project_id = task.project_id
        return redirect('project_manager:tasks', project_id=project_id)

    context = {
        'task': task,
        'project': task.project
    } 

    return render(request, 'project_manager/edit_task.html', context = context)

def delete_task(request, task_id):
    task = m.Task.objects.get(id=task_id)
    task.delete()
    project_id = task.project_id
    return redirect('project_manager:tasks', project_id=project_id)