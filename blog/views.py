from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail

# Create your views here.

def index(request):
    books = models.Post.publishedBooks.all()
    paginator = Paginator(books, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})


def detail(request, year, month, day, title):
    post = get_object_or_404(models.Post, 
    publish__year = year,
    publish__month = month,
    publish__day = day,
    slug = title,
    status = 'published')

    comments = post.comments.filter(active=True)
    form = CommentForm()

    if request.method == 'GET':
        context = {'post':post,'comments':comments, 'form':form }
    
    else:
        comment = CommentForm(request.POST)
        if comment.is_valid():
            newComment = comment.save(commit=False)
            newComment.post = post
            newComment.save()
            context = {'post':post, 'comments':comments, 'form':form}

    return render(request, 'details.html', context)

def sharePost(request, postId):
    post = get_object_or_404(models.Post, id=postId, status = 'published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            message = cd['your_name'] + ' recommends you reading ' + post.title + ' at ' + post_url
            sent = send_mail(
                'Recommendations',
                message,
                cd['email'],
                [cd['to']],
                fail_silently=False,
            )
    
    else:
        form = EmailPostForm()
    return render(request, 'share.html', {'post':post, 'form':form, 'sent':sent})