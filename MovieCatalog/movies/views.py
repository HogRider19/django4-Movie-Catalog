from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie


class HomeView(ListView):
    """Класс отображения фильмов на главной странице"""
    model = Movie
    template_name = 'movies/home.html'
    context_object_name = 'movies'
    paginate_by = 9
    
