from django.urls import path
from . import views

app_name = 'project_manager'

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:project_id>/edit', views.edit_project, name='edit_project'),
    path('<int:project_id>/delete', views.delete_project, name='delete_project'),

    path('tasks/<int:project_id>', views.tasks, name='tasks'),
    path('task/<int:task_id>/edit', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete', views.delete_task, name='delete_task'),    
]