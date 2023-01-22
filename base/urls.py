from django.urls import path
import base.views as base_views

urlpatterns = [
    path("" , base_views.homePage , name ="home-page") , 
    path("post-loader/" , base_views.postLoader , name ="post-loader") , 
]