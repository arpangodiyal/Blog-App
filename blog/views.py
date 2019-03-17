from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    books = models.Post.publishedBooks.all()
    paginator = Paginator(books, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})

# def detail(request, title):
#     title = title
#     post = get_object_or_404(models.Post, slug = title)
#     print(post)

def detail(request, year, month, day, title):
    post = get_object_or_404(models.Post, 
    publish__year = year,
    publish__month = month,
    publish__day = day,
    slug = title,
    status = 'published')

    context = {'post':post}
    return render(request, 'details.html', context)
