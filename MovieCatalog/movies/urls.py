from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('movie/<slug:slug>/', views.MovieDetail.as_view(), name='moviedetail'),
    path('category/<str:category_id>', views.CategoryView.as_view(), name='categoryview'),
    path('search/', views.Search.as_view(), name='search'),
    path("add_rating/", views.AddStarRating.as_view(), name='add_rating'),
    path('createreview/<int:pk>/', views.CreateReview.as_view(), name='createreview'),
    path('filter/', views.FilterMovies.as_view(), name='filter'),
    path('actor/<str:slug>/', views.ActorDetail.as_view(), name='actorview'),
]