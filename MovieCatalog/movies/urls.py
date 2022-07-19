from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('movie/<slug:slug>/', views.MovieDetail.as_view(), name='moviedetail')
]