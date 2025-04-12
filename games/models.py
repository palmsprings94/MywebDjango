from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Hangman(models.Model):
    category = models.CharField(default=None, max_length=25)
    words = models.TextField(default=None)
    nonletters = models. CharField(default=None, max_length=50)

    def __str__(self): return self.category

class Hangmansesh(models.Model):
    category = models.CharField(default=None, max_length=25)
    word = models.CharField(default=None)
    nonletters = models.CharField(default=None, max_length=50)
    guesses = models.TextField(default=None)
    disp = models.CharField(default=None)
    lives = models.IntegerField(default=3)

    def __str__(self): return self.word

class Oregontrailstops(models.Model):
    index = models.IntegerField(default=None)
    name = models.CharField(default=None)
    def __str__(self): return self.name

class Oregontrailevents(models.Model):
    name = models.CharField(default=None)
    chances = models.IntegerField()
    numeffect = models.IntegerField()
    def __str__(self): return self.name

