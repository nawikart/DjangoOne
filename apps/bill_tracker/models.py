from django.db import models
import apps.user.models as mu

# Create your models here.
class Bill(models.Model):
    description = models.CharField(max_length=64)
    amount = models.IntegerField()
    user = models.ForeignKey(mu.User, related_name='bills', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)