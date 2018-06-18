from django.db import models
import apps.user.models as mu

class Project(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(mu.User, related_name='projects', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task(models.Model):
    description = models.CharField(max_length=256)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    