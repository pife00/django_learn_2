from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required 

# Create your views here.
from .models import Champion,Favorites
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
           item.created_by = request.user
           item.save()
           return redirect('tasks:detail',name= item.name)
    else:
        form = ChampionForm()
    return render(request,'tasks/form.html',{
        'form':form
    })

@login_required
def favorite(request,name):
    champion = get_object_or_404(Champion,name=name)
    item = Favorites(user=request.user,name=champion,is_active=True)
    item.save()
    """ //item = get_object_or_404(Favorites,name=name)
    print(item)
     """
    return redirect('core:index')
    
    
    