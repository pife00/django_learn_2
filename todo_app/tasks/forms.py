
from django import forms

from .models import Champion

class ChampionForm(forms.ModelForm):
    class Meta:
        model = Champion
        fields = ('category','name','description','imgUrl','is_OP')

        widgets = {
            'category':forms.Select(attrs={
                "class":" mt-2 w-full p-3 border border-gray-300 block rounded-xl"
            }),
            'name':forms.TextInput(attrs={
                "class":"mt-2 w-full p-3 border border-gray-300 block rounded-xl"
            }),
             'description':forms.Textarea(attrs={
                "class":"mt-2 w-full p-3 border border-gray-300 block rounded-xl"
            }),
             'imgUrl':forms.TextInput(attrs={
                "class":"mt-2 w-full p-3 border border-gray-300 block rounded-xl"
            })
        }

    