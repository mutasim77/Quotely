from django.shortcuts import render
from .models import *

def main(request):

    posts = Post.objects.all()
    return render(request, 'base/main.html', {'posts': posts})