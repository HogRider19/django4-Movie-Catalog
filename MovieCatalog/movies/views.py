from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Movie, Review, Actor, Genre
from .forms import ReviewForm
from django.db.models import Q


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

    def get_queryset(self):
        return Movie.objects.filter(
            slug=self.kwargs.get('slug')).prefetch_related(
                'directors').prefetch_related('actors').select_related('genre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context


class FilterMovies(ListView):
    """Класс фильтрации фильмов"""
    model = Movie
    template_name = 'movies/home.html'
    context_object_name = 'movies'
    paginate_by = 9

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genre__in=self.request.GET.getlist('genre'))
        )
        return queryset


class CreateReview(CreateView):
    """Класс создания отзыва к фильму"""
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.movie_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.movie.get_absolute_url()


class ActorDetail(DetailView):
    """Класс вывода информации об актере"""
    model = Actor
    template_name = 'movies/actor.html'
    context_object_name = 'actor'
    slug_field = 'name'

    def get_queryset(self):
        return Actor.objects.filter(name=self.kwargs.get('slug'))