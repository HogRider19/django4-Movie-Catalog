from django.shortcuts import render
from rest_framework import generics
from movies.models import Movie
from .serializers import MovieSerializer


class MovieAPIList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

