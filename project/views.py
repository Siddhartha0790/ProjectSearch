from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm,ReviewForm
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .utils import pagination
from django.contrib import messages




def projects(request):
    search_query=""
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    projects = Project.objects.filter(
        Q(name__icontains = search_query) |
        Q(description__icontains = search_query) |
        Q(owner__name__icontains = search_query)
    )
    
    custom_range,newprojects = pagination(request , projects)
        
    context = {
        'projects': newprojects,
        'search_query':search_query,
        
        'custom_range': custom_range
        
    }
    return render(request, 'project/projects.html', context)

def project(request, pk):
    review = ReviewForm()
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        review= ReviewForm(request.POST)
        if review.is_valid():
            try:
                 addreview = review.save(commit = False)
                 addreview.owner = request.user.profile
                 addreview.project = project
                
                 addreview.save()
                 
                 Project.votecount
                 messages.success(request, 'Your review was successfully added! ')
                 return redirect('project', pk=project.id)
            except :
                messages.error(request, 'Cannot Add another review !')
                return redirect('project', pk=project.id)
                
       
    
    return render(request, 'project/project.html', {'project': project , 'review':review,})


@login_required(login_url = 'login')
def projectCRUD(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        project = form.save(commit=False)
        project.owner = profile
        project.save()
        return redirect('projects')
    
    return render(request , 'project/project_create.html', {'form':form})


@login_required(login_url = 'login')
def projectUpdate(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        form.save()
        return redirect('account')
    return render(request , 'project/project_create.html', {'form':form})


@login_required(login_url = 'login')
def projectDelete(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project = Project.objects.get(id=pk)
        project.delete()
        return redirect('account')
    return render(request,'project/project_delete.html', {'project': project})
    
    
        
        