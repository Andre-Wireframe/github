from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola, name='hola'),
    path('AddPost/', views.AddPost.as_view(), name='AddPost'),
    path('AddComment/', views.AddComment.as_view(), name='AddComment'),
]