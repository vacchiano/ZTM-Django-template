import re
from django.http import HttpResponse
from django.shortcuts import render

my_movies = [
    {
        "title": "top gun"
    },
    {
        "title": "lord of the rings"
    },
    {
        "title": "star wars"
    }
]

def index(request):
    context = {
        "my_movies": my_movies
    }
    return render(request, "movies/index.html", context)

def about(request):
    return render(request, "movies/about.html")