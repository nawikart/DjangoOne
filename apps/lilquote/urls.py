from django.urls import path
from . import views

app_name = 'lilquote'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:user_id>/quotes', views.user_quotes, name='user_quotes'),

    path('search', views.search, name='search'),
    path('result/<query>', views.result, name='result'),
]