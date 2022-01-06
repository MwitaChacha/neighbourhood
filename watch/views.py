from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    
    return render(request, 'index.html')