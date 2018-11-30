from django.shortcuts import render
from .models import Video
from django.utils import timezone

# Create your views here.
def home_index(request):
    return render(request, 'home/index.html', {})


def home_youtube(request):
    videos = Video.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home/youtube.html', {'videos':videos})


def home_spaceinvaders(request):
    return render(request, 'home/spaceinvaders.html', {})
