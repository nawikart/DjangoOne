from django.db import models
import apps.user.models as mu


# Create your models here.
class Quote(models.Model):
    content = models.CharField(max_length=256)
    user = models.ForeignKey(mu.User, related_name='quotes', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
