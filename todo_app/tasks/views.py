from django.shortcuts import redirect, render,get_object_or_404

# Create your views here.
from .models import Champion
from .forms import ChampionForm

def detail(request,name):
    item = get_object_or_404(Champion, name=name)
    return render(request,'tasks/detail.html',{
        'item':item
    })

def newChampion (request):
    if request.method == "POST":
        form = ChampionForm(request.POST,request.FILES)
        if form.is_valid():
           item = form.save(commit=False)
           item.created_by = 'admin'
           item.save()
           return redirect('tasks:detail',name= item.name)
    else:
        form = ChampionForm()
    return render(request,'tasks/form.html',{
        'form':form
    })

    
    