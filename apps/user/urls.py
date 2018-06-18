from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    path('user/register', views.register, name='register'),
    path('user/logout', views.logout, name='logout'),
]