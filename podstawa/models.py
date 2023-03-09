from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import null
# Create your models here.
class Zadanie(models.Model):
    nazwa=models.CharField(max_length=255,null=True,blank=True)
    opis=models.TextField(null=True,blank=True)
    status=models.BooleanField(default=False)
    data_roz=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    
    #czas_zakonczenia = models.DateTimeField()
    
    
    def __str__(self):
        return self.nazwa
    
    class Meta:
        ordering =['status']
        
