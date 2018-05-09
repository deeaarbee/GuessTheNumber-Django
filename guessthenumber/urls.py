
from django.contrib import admin
from django.urls import path,include

from guess.urls import guessurl

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += guessurl