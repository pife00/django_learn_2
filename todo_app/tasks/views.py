from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required 

# Create your views here.
from .models import Champion,Favorites
from .forms import ChampionForm

def detail(request,name):
    item = get_object_or_404(Champion, name=name)
    userFavorite = False
    if(request.user.is_authenticated):
        favorite = Favorites.objects.filter(name=name,user=request.user)
        if favorite.exists():
            first = favorite.first()
            userFavorite = first.is_active

    return render(request,'tasks/detail.html',{
        'item':item,
        'is_favorite':userFavorite   
    })

@login_required
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
    itemExist = Favorites.objects.filter(name=name,user=request.user)

    if itemExist.exists():
        favorite = itemExist.first()
        favorite.is_active = not favorite.is_active
        itemExist.update(is_active = favorite.is_active)

    else:
        item = Favorites(user=request.user,name=champion,is_active=True)
        item.save()

    return redirect('tasks:detail',name=name)
    
def favoritesList(request):
    items = Favorites.objects.all()
    return render(request,'tasks/favorites_list.html')  
    