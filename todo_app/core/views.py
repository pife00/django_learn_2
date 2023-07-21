from django.shortcuts import render,get_list_or_404

# Create your views here.

from tasks.models import Champion

def index(request):
    item = Champion.objects.all()
    return render(request,'core/index.html',{
        'items':item
    })


