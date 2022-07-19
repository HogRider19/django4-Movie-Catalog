from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


class HomeView(ListView):
    """Класс отображения фильмов на главной странице"""
    model = Movie
    template_name = 'movies/home.html'
    context_object_name = 'movies'
    paginate_by = 9


class MovieDetail(DetailView):
    """Класс отображение выбранного фильма"""
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
    
