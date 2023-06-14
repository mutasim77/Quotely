from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def main(request):
    
    #? If the HTTP request method is POST (when we submit the form), it stores new data in the database
    if request.method == "POST":
        post = Post()
        post.author = request.POST.get('author')
        post.content = request.POST.get('content')
        post.image = request.FILES['image']
        
        post.save()
        return redirect('/')

    posts = Post.objects.all()
    return render(request, 'base/main.html', {'posts': posts})