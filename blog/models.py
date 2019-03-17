from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from . import views

# Create your models here.

class PublishedBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ['-publish']

    publishedBooks = PublishedBookManager()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse(views.detail, args=[self.publish.year,
                        self.publish.strftime('%m'),
                        self.publish.strftime('%d'),
                        self.slug])
        # return reverse(views.detail, args=[self.slug])

    def __str__(self):
        return self.title


