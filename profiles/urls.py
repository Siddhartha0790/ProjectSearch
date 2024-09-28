from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import profiles,profile,loginPage,logoutUser,registerUser,accountPage,editProfile,sendmessage
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    
    path('', profiles, name='profiles'),
    path('profile/<int:pk>/' ,profile ,name='profile'),
    path('login/',loginPage, name='login'),
    path('logout/',logoutUser , name='logout'),
    path('register/',registerUser, name= 'register'),
    path('account/',accountPage, name= 'account'),
    path('editprofile/',editProfile,name = 'edit'),
    path('sendmessage/<int:pk>' ,sendmessage,name='sendmessage' )
]

