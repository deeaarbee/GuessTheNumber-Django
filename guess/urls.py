from django.contrib import admin
from django.urls import path,include
from .views import hello,guess

guessurl = [
    path('hello/',hello,name="hello"),
    path('guess/', guess, name="guess")

]