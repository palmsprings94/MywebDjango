from django.urls import path
from games import views
urlpatterns = [
    path('', views.games, name='games'),
    path('hangman/', views.hangman, name='hangman'),
    path('oregontrail/', views.Oregontrail, name='oregontrail'),
]