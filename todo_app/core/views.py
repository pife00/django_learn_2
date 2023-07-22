from django.shortcuts import render,get_list_or_404,redirect

# Create your views here.

from tasks.models import Champion
from . forms import SingUpForm,LoginForm

def index(request):
    item = Champion.objects.all()
    return render(request,'core/index.html',{
        'items':item
    })

def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SingUpForm()
    return render(request,'core/signup.html',{
        'form':form
    })



