from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Первый автор',
        'title': 'Первый пост в блоке',
        'content': 'Контент первого поста',
        'date_posted': '06 августа 1999'
    },
    {
        'author': 'Второй автор',
        'title': 'Второй пост в блоке',
        'content': 'Контент второго поста',
        'date_posted': '07 августа 1999'
    },
    {
        'author': 'Третий автор',
        'title': 'Третий пост в блоке',
        'content': 'Контент третьего поста',
        'date_posted': '08 августа 1999'
    },
    {
        'author': 'Четвёртый автор',
        'title': 'Четвёртый пост в блоке',
        'content': 'Контент четвёртого поста',
        'date_posted': '09 августа 1999'
    },
    {
        'author': 'Четвёртый автор',
        'title': 'Четвёртый пост в блоке',
        'content': 'Контент четвёртого поста',
        'date_posted': '10 августа 1999'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
