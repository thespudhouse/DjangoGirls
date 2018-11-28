from django.shortcuts import render

# Create your views here.
def home_index(request):
    return render(request, 'home/index.html', {})


def home_youtube(request):
    return render(request, 'home/youtube.html', {})


def home_spaceinvaders(request):
    return render(request, 'home/spaceinvaders.html', {})
