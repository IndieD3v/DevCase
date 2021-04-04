from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage
from .models import Projects
from .forms import NewProject


def Home(request):
    user = request.user.username
    projects = Projects.objects.all()

    p = Paginator(projects,9)
    page_num = request.GET.get('page',1)

    page = p.page(page_num)
    
    return render(request,'base/home.html',{

        'projects':page,
        'user':user,
        
    })


def Add(request):
   
    if request.method == 'POST':
        form = NewProject(request.POST,request.FILES)
        
        if form.is_valid():
            project = form.save(commit=False)

            project.name = form.cleaned_data['project_name']
            project.url = form.cleaned_data['url']
            project.description = form.cleaned_data['description']
            project.author = request.user
            

            project.save()
            
            return redirect('home')
        else: 
            return render(request,'tasks/add.html',{
                    "form":form  
            })

    return render(request,'base/add.html',{
        'form':NewProject(),
    })

def Delete(request,pk):

    project = Projects.objects.get(id=pk)
    project.delete()
        
    return redirect('home')


def Update(request,pk):
    project = Projects.objects.get(id=pk)

    form = NewProject(instance=project)

    if request.method == 'POST':
        form = NewProject(request.POST,request.FILES,instance=project)

        if form.is_valid():
            form.save()

        return redirect('home')
    
    return render(request,'base/update.html',{'form':form})


def LikeProject(request):
    user = request.user
    project = get_object_or_404(Projects, id = request.POST.get('project_id'))

    if user in project.like.all():
        project.like.remove(user)
    else:
        project.like.add(user)

    return redirect('home')

    
def Logout(request):
    logout(request)

    return redirect('home')
    
