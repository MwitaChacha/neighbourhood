from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile =Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('update_profile')
    profiles = Profile.objects.filter(id = current_user.id).all()
    hoods = NeighbourHood.objects.all().order_by('-posted_at')    
    return render(request, 'index.html',{"profiles": profiles, "hoods":hoods})



@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request, 'update-profile.html', {'form': form})
 
 

@login_required(login_url='/accounts/login/')
def profile(request,pk):
    user = User.objects.get(pk = pk)
    profiles = Profile.objects.filter(user = user).all()
    current_user = request.user
    return render(request,'profile.html',{"current_user":current_user, "user":user, "profiles":profiles})
 


@login_required(login_url='/accounts/login/')
def createhood(request):
    current_user = request.user
    form = HoodForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = request.user
            hood.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request,'create-hood.html',{'form':form})
 