from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from .forms import NewPostForm
from .models import User,NewPost,Profile
import json


def index(request):
    posts = NewPost.objects.all().order_by("-timestamp")
    
    if request.user.is_authenticated:
        if request.method == "POST":
            post = NewPostForm(request.POST)
            user = request.user
            timestamp = datetime.now()
            if post.is_valid:
                post = post.save(commit=False)
                postdata = NewPost(post=post,user=user,timestamp=timestamp)
                postdata.save()

            return render(request,"network/index.html",{
                "post" : post,
                "user" : user,
                # "posts" : posts,
                "timestamp" : timestamp
            })
            # JsonResponse(posts, safe=False)

        else:
            post = NewPostForm()
            return render(request,"network/index.html",{
                "post" : post,
                "posts" : posts
            })

    return render(request,"network/index.html",{
        "posts" : posts
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def profilepage(request,id):
    user = User.objects.get(pk=id)
    profile = Profile.objects.filter(user = user)
    posts = NewPost.objects.filter(user = user).order_by("-timestamp")
    return render(request, "network/profile.html",{
        "user" : user,
        "profile" : profile,
        "media_url" : settings.MEDIA_URL,
        "posts" : posts
    })