from django import template
from movies.models import Category, Movie, Genre


register = template.Library()


@register.simple_tag()
def get_genres():
    """Получение всех жанров фильмов"""
    return Genre.objects.all()


@register.simple_tag()
def get_years():
    """Получение всех дат выхода фильмов"""
    return Movie.objects.values('year').distinct()


@register.inclusion_tag('include/tags/categories_drop_down.html')
def get_category_drop_down():
    """Рендер всплывающего меню с категориями в меню"""
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('include/tags/last_movies.html')
def get_last_movies():
    """Рендер поля с последними добавленными фильмами"""
    last_movies = Movie.objects.all().order_by('-year')[:5]
    return {'movies': last_movies}
