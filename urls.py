from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_ranking_view, name='resume_ranking'),
]