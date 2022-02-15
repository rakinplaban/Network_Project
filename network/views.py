from sqlite3 import Timestamp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import IntegrityError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect 
from django.urls import reverse
from datetime import datetime
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .serializers import EditPostSerializer
from .forms import NewPostForm
from .models import User,NewPost,Profile
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator


# @api_view(['GET','POST'])
def index(request):
    posts = NewPost.objects.all().order_by("-timestamp")
    page = Paginator(posts,3)
    page_req = request.GET.get('page')
    page_view = page.get_page(page_req)
    num = "a" * page_view.paginator.num_pages
    
    if request.user.is_authenticated:
        if request.method == "POST":
            post = NewPostForm(request.POST)
            user = request.user
            timestamp = datetime.now()
            if post.is_valid:
                post = post.save(commit=False)
                postdata = NewPost(post=post,user=user,timestamp=timestamp)
                postdata.save()
                # return Response({"message" : "Post created successfully 😊!"})

            return render(request,"network/index.html",{
                "post" : post,
                # "user" : user,
                # "posts" : posts,
                "timestamp" : timestamp,
                "page_view" : page_view,
                "num" : num,
                # "like" : like,
            })
            # JsonResponse(posts, safe=False)

        else:
            post = NewPostForm()
            return render(request,"network/index.html",{
                "post" : post,
                "posts" : posts,
                "page_view" : page_view,
                "num" : num,
                # "like" : like,
            })

    return render(request,"network/index.html",{
        "posts" : posts,
        "page_view" : page_view,
        "num" : num,
        # "like" : like,
    })

@login_required

def likepost(request,posts_id):
    posts = NewPost.objects.get(id = posts_id)
    is_like = False
    for like in posts.likepost.all():
        if like == request.user and request.method == "POST":
            is_like = True
            break
    
    if not is_like:
        posts.likepost.add(request.user)
    
    else:
        posts.likepost.remove(request.user)
    posts.save()
    # serialize_obj = serializers.serialize("json",posts_id)
    
    return JsonResponse({
        "is_like" : is_like,
        "num_like" : posts.likepost.count()
    },safe=200)
    
    # return render(request,"network/index.html",{
    #     "is_like" : is_like,
    #     # "like_num" : like_num,
    # })
    

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

@login_required
def createpost(request):
    postform = NewPostForm()
    if request.method == "POST":
        post = NewPostForm(request.POST)
        user = request.user.id
        timestamp = datetime.now()
        if post.is_valid:
            post = post.save(commit=False)
            postdata = post.save(post=post,user = user,timestamp = timestamp)
            postdata.save()
            return HttpResponseRedirect(reverse("index"))
            # return Response({
            #     "message":"Post successfully created 😊",
            #     "post": post,
            #     "user" : user,
            #     "timestamp" : timestamp
            # })

    return render(request,"network/postform.html",{
        "postform" : postform
    })

@login_required
def editpost(request,id):
    mainpost = get_object_or_404(NewPost,id = id)
    postform = NewPostForm(instance = mainpost)
    if request.method == "POST":
        postform = NewPostForm(request.POST, instance= mainpost)
        timestamp = datetime.now()
        if postform.is_valid():
            postform.instance.timestamp = datetime.now()
            postform.save()
            return redirect("index")

    return render(request,"network/editform.html",{
        "postform" : postform,
        "mainpost" : mainpost,
        "id" : id,
    })

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
    page = Paginator(posts,3)
    page_req = request.GET.get('page')
    page_view = page.get_page(page_req)
    num = "a" * page_view.paginator.num_pages
    return render(request, "network/profile.html",{
        "user" : user,
        "profile" : profile,
        "all_followers" : all_followers,
        "is_following" : is_following,
        "all_following" : all_following,
        "is_followed" : is_followed,
        "media_url" : settings.MEDIA_URL,
        "posts" : posts,
        "page_view" : page_view,
        "num" : num,
    })

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

    posts = NewPost.objects.filter(user__in = followings).order_by("-timestamp")
    page = Paginator(posts,3)
    page_req = request.GET.get('page')
    page_view = page.get_page(page_req)
    num = "a" * page_view.paginator.num_pages

    return render(request,"network/following.html",{
        "user" : user,
        "profile" : profile,
        "followings" : followings,
        "posts" : posts,
        "page_view" : page_view,
        "num" : num,
    })

def view_post(request,id):
    post = NewPost.objects.get(id=id)
    user = request.user
    # timestamp = 
    is_like = False
    for like in post.likepost.all():
        if like == request.user and request.method == "POST":
            is_like = True
            break
    
    if not is_like:
        post.likepost.add(request.user)
    
    else:
        post.likepost.remove(request.user)
    
    return JsonResponse({
        "is_like" : is_like,
        "like_num" : post.likepost.count()
    })
    return render(request,"network/postpage.html",{
        "post" : post,
        "user" : user,
    })