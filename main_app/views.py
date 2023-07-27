from django.shortcuts import render
from .models import Cat


# Create your views here.

# Define the home view


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# Add new view


def cats_index(request):
    cats = Cat.objects.all()
    # We pass data to a template very much like we did in Express!
    return render(request, 'cats/index.html', {
        'cats': cats
    })


def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})
