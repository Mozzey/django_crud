from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Mozzey',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': '1 1 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': '2 2 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
