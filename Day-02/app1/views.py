from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def list(request):
    items = ["Django", "React", "PostgreSQL", "Docker"]
    return render(request, "list.html",{"items": items}) 
