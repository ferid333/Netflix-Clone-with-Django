import uuid
from django.shortcuts import render,redirect
from .models import Profile,Movie
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect("profiles")
    return render(request,"index.html")


def profile(request):
    if not request.user.is_authenticated:
        return redirect("home")
    profiles=request.user.profiles.all()
    context={
        "profiles":profiles
    }
    return render(request,"profilelist.html",context)    

def create_new_profile(request):
    if not request.user.is_authenticated:
        return redirect("home")
    if request.method=="POST":
        name=request.POST["name"]
        age_limit=request.POST["age_limit"]
        new_profile=Profile.objects.create(name=name,age_limits=age_limit.upper())
        new_profile.save()
        request.user.profiles.add(new_profile)
        return redirect("profiles")
    return render(request,"createprofile.html")


def mainpage(request,profile_id):
    if not request.user.is_authenticated:
        return redirect("home")
    try:
        profile=Profile.objects.get(uuid=profile_id)
        movies=Movie.objects.filter(age_limits=profile.age_limits)
        showcase=movies[0]
    except:
        showcase=None
    if profile not in request.user.profiles.all():
        return redirect("profiles")
    context={
        "movies":movies,
        "showcase":showcase
    }
    return render(request,"movielist.html",context)


def show_movie_detail(request,movie_id):
    if not request.user.is_authenticated:
        return redirect("home")
    movie=Movie.objects.get(uuid=movie_id)
    context={
        "movie":movie
    }
    return render(request,"moviedetail.html",context)


def watchmovie(request,movie_id):
    if not request.user.is_authenticated:
        return redirect("home")
    movie=Movie.objects.get(uuid=movie_id)
    context={
        "movie":list(movie.videos.values())
    }
    return render(request,"watchmovie.html",context)                