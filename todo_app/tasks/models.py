from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.name

class Champion(models.Model):
    category = models.ForeignKey(Categories,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255),
    descrption = models.CharField(blank=True,null=True),
    imgUrl = models.CharField(max_length=255),
    price = models.FloatField(),
    is_OP = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE),
    
    
    
        