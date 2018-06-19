from django.urls import path
from . import views

app_name = 'tv_guide'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/unlike/<destination>', views.unlike, name='unlike'),
    path('<int:id>/like/<destination>', views.like, name='like'),
    path('search', views.search, name='search'),
    path('result/<query>', views.result, name='result'),
]