# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100, default='')
    team=models.CharField(max_length=50, default='')
    description= models.TextField(max_length=200)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField(upload_to='img')
    
    
    def __str__(self):
        return self.name
        
       