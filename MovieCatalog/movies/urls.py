from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('movie/<slug:slug>/', views.MovieDetail.as_view(), name='moviedetail'),
    path('createreview/<int:pk>/', views.CreateReview.as_view(), name='createreview'),
    path('filter/', views.FilterMovies.as_view(), name='filter'),
    path('actor/<str:slug>/', views.ActorDetail.as_view(), name='actorview'),
]