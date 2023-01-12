from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path('directors/', views.director_list, name='director_list'),
    path('directors/<int:director_id>/', views.director_detail, name='director_detail'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail')
]