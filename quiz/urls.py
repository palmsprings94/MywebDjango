from django.urls import path
from quiz import views as quiz_views

urlpatterns = [
    path('', quiz_views.quiz, name='quiz'),
    path('addquestions/',quiz_views.addquestions, name='addquestions'),
    path('beginnerquiz/', quiz_views.beginnerquiz, name='beginnerquiz'),
    path('addquestionsbeg/',quiz_views.addquestionsbeginner, name='addquestionsbeginner'),
]