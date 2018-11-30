from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Video


# Create your views here.
def home_index(request):
    return render(request, 'home/index.html', {})


def home_youtube(request):
    videos = Video.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home/youtube.html', {'videos':videos})


def home_spaceinvaders(request):
    return render(request, 'home/spaceinvaders.html', {})

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from mysite.core.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})