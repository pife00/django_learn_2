from django.contrib import admin

# Register your models here.

from .models import Categories,Champion

admin.site.register(Categories)
admin.site.register(Champion)



