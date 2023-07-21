from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Champion

def detail(request,name):
    item = get_object_or_404(Champion, name=name)
    return render(request,'tasks/detail.html',{
        'item':item
    })
    
    