from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect 
from django.urls import reverse
from datetime import datetime
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .serializers import EditPostSerializer
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
    followers = user.profile.followers.all()
    followings = user.profile.followings.all()
    is_following = False
    for follower in followers:
        if follower == request.user:
            is_following = True
            break
        else:
            is_following = False

    is_followed = False
    for following in followings:
        if following == request.user:
            is_followed = True
            break
        else:
            is_followed = False
    all_followers = len(followers)
    all_following = len(followings)
    posts = NewPost.objects.filter(user = user).order_by("-timestamp")
    return render(request, "network/profile.html",{
        "user" : user,
        "profile" : profile,
        "all_followers" : all_followers,
        "is_following" : is_following,
        "all_following" : all_following,
        "is_followed" : is_followed,
        "media_url" : settings.MEDIA_URL,
        "posts" : posts
    })

# def followerCount(request,id):
#     profile = Profile.objects.get(pk = id)
#     followers = profile.followers.all()
#     all_followers = len(followers)

def followersPeople(request,id):
    user = User.objects.get(pk = id)
    profile = Profile.objects.filter(user = user)
    user.profile.followers.add(request.user)
    request.user.profile.followings.add(user)

    return redirect('profile', id = id)

def followersRemove(request,id):
    user = User.objects.get(pk = id)
    profile = Profile.objects.filter(user = user)
    user.profile.followers.remove(request.user)
    request.user.profile.followings.remove(user)

    return redirect('profile', id = id)

def followerspost(request):
    user = request.user
    profile = Profile.objects.filter(user = user)
    followings = user.profile.followings.all()
    # for following in followings:
    #     posts = NewPost.objects.filter(user = following)

    posts = NewPost.objects.filter(user__in = followings).order_by("-timestamp")

    return render(request,"network/following.html",{
        "user" : user,
        "profile" : profile,
        "followings" : followings,
        "posts" : posts,
    })
