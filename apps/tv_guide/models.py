from django.db import models
import apps.user.models as mu

class Movie(models.Model):
    api_id = models.IntegerField(unique=True)
    url = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=256)

    # def parse_json(self, data):
    #     self.api_id = data['id']
    #     self.url = data['url']
    #     self.name = data['name']
    #     if data['image'] != None:
    #         self.image = data['image']['original']    


class Like(models.Model):
    user = models.ForeignKey(mu.User, related_name='likes', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='likes', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)            