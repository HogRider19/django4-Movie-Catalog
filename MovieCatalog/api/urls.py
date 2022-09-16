from django.urls import path
from . import views


urlpatterns = [
    path('movie/', views.MovieAPIList.as_view()),
]