from django.db import models


class Category(models.Model):
    """Модель категорий"""
    title = models.CharField('Категория', max_length=100)
    description = models.TextField('Описание')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    """Класс актеров и режиссеров"""
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveIntegerField('Возраст', blank=True, null=True)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актеры и режисеры'
        verbose_name_plural = 'Актеры и режисеры'


class Genre(models.Model):
    """Модель жанров"""
    title = models.CharField('Жанр', max_length=100)
    description = models.TextField('Описание')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    """Класс фильмов"""
    name = models.CharField('Название', max_length=250)
    tagline = models.CharField('Слоган', max_length=100, default='')
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='posters/')
    year = models.DateField('Дата выхода')
    country = models.CharField('Страна', max_length=250)
    directors = models.ManyToManyField(
        Actor, verbose_name='Режиссер', related_name='film_director')
    actors = models.ManyToManyField(
        Actor, verbose_name='Актеры', related_name='film_actor')
    world_premiere = models.DateField('Дата выхода', blank=True, null=True)
    budget = models.PositiveIntegerField('Бюджет', blank=True, null=True)
    fees_in_use = models.PositiveIntegerField(
        'Сборы в США', blank=True, null=True)
    fees_in_world = models.PositiveIntegerField(
        'Сборы в мире', blank=True, null=True)
    category = models.ManyToManyField(
        Category, verbose_name='Категория', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShorts(models.Model):
    """Кадры из фильма"""
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movieShorts/')
    movie = models.ForeignKey(
        Movie, verbose_name='Фильм', related_name='shorts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    """Модель оценки"""
    value = models.PositiveIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class Rating(models.Model):
    """Модель рейтинга"""
    ip = models.CharField('ip адрес', max_length=15)
    star = models.ForeignKey(
        RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name='Фильм', related_name='rating')

    def __str__(self):
        return f"{self.movie} - {self.star}"

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class Review(models.Model):
    """Модель отывов"""
    email = models.EmailField('Почта', max_length=250)
    name = models.CharField('Имя', max_length=250)
    text = models.TextField('Сообщение')
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.CASCADE, blank=True, null=True)
    movie = models.ForeignKey(
        Movie, verbose_name='Фильм', related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    
