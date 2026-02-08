from django.shortcuts import render
from .models import Blogpost
def show_posts(request):
    posts= Blogpost.objects.all()
    
    return render(request, 'posts.html', {'posts': posts})
    
