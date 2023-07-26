from django.urls import path

from . import views 

app_name = 'tasks'

urlpatterns = [
    path('<str:name>/',views.detail,name='detail'),
    path('add/new-champion/',views.newChampion,name="new-champion"),
    path('favorite/favorites-list/',views.favoritesList,name="list"),
    path('<str:name>/favorite/',views.favorite,name='favorite'),
]
