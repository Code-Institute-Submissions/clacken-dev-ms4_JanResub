from django.shortcuts import render
from .models import Image

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def gallery(request):
    """ A view to show all gallery images """

    images = Image.objects.all()

    context = {
        'images': images,
    }

    return render(request, 'home/gallery_copy.html', context)