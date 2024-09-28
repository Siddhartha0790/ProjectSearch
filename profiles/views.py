from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm,ProfileEditForm,sendMessageForm
from django.db.models import Q
from .utils import pagination

from django.contrib.auth.decorators import login_required
# Create your views here.
def profile(request,pk):
    profile= Profile.objects.get(id=pk)
    return render(request, 'profiles/profilepage.html',{'profile':profile})

def profiles(request):
    search_query= ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print( 'Search: ' + search_query)
    profiles= Profile.objects.filter(Q(name__icontains= search_query) | Q(shortbio__icontains = search_query))
    
    custom_range,newprofiles = pagination(request, profiles)
    context = {
        'profiles':newprofiles,
        'search_query' : search_query,
        'custom_range': custom_range
    }
    return render(request , 'profiles/profiles.html',context )


@login_required(login_url='login')
def accountPage(request):
    Profile = request.user.profile
    return render(request, 'profiles/accountPage.html', {'profile':Profile})
    

def loginPage(request):
    if request.user.is_authenticated :
        return redirect('profiles')
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        try:
            user = User.objects.get( username = username )
        except:
            messages.error(request , 'username dont exist')
        user = authenticate(request,username = username,password=password)
        if user is not None:
           login(request, user) 
           messages.success(request, 'You are now logged in as ' + user.username )
           return redirect('account')
        else : 
           messages.error(request,'incorrect username or password')
    
    return render(request , 'profiles/loginpage.html',{'type':'login'})
        
def logoutUser(request):
    logout(request)
    messages.info(request , 'User was logges out! ')
    return redirect('login')
           
def registerUser(request):
    context = {}
    form = RegisterForm()
    if request.method == 'POST':
        
        form = RegisterForm(request.POST)
        if form.is_valid():
           
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User is created!')
            return redirect('profiles')
        else :
            messages.error(request,'Some error occurred , try again!')
    else :
       
        context = {'type':'register','form':form}
    return render(request , 'profiles/loginpage.html', context)
@login_required(login_url='login')
def editProfile(request):
    user = request.user.profile
    form = ProfileEditForm(instance = user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST,request.FILES, instance = user)
        if form.is_valid():
            form.save()
            return redirect('account')
        else :
            messages.error('An error occured please try again! ')
        
    return render(request , 'profiles/profileEdit.html', {'form':form})


@login_required(login_url='login')
def sendmessage(request,pk):
    form = sendMessageForm()
    receiver = Profile.objects.get(id=pk)
    sender = request.user.profile
    if request.method == 'POST':
        form = sendMessageForm(request.POST)
        if form.is_valid():

                form2 = form.save(commit=False)
                form2.owner = sender
                form2.receiver = receiver
                form2.save()
                return redirect('profiles')
            
    return render(request , 'profiles/sendmessage.html', {'form':form})
    
