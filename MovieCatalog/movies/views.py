from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Movie, Review, Actor, Genre, Rating
from .forms import ReviewForm, RatingForm
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
        context['star_form'] = RatingForm()
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


class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)