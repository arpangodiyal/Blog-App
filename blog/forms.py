from django import forms
from django.forms import ModelForm
from . import models

class EmailPostForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email address')
    to = forms.EmailField(label="Recepient's email address")
    comment = forms.CharField(required = False, widget = forms.Textarea)

class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body']
