
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:id>",views.profilepage,name="profile"),
    path("profile/<int:id>/following/addfollower",views.followersPeople,name="addfollower"),
    path("profile/<int:id>/following/removefollower",views.followersRemove,name="removefollower"),
    path("postform", views.createpost, name="postform"),
    path("editform/<int:id>",views.editpost,name="editpost"),
    path("following",views.followerspost,name="following"),
    path("index/<int:id>/like",views.likepost, name="like"),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
