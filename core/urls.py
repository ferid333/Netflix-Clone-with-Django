from django.urls import path
from . import views

urlpatterns=[
   path("",views.index,name="home"),
   path("profile/",views.profile,name="profiles"),
   path("profile/create/",views.create_new_profile,name="createprofile"),
   path("mainpage/<str:profile_id>/",views.mainpage,name="mainpage"),
   path("moviedetail/<str:movie_id>/",views.show_movie_detail,name="moviedetail"),
   path("watch/<str:movie_id>",views.watchmovie,name="watchmovie")
]