# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse 
from home.views import index
from .forms import UserContactForm, SalesForm
from django.core.mail import send_mail
from django.conf import settings
from .models import contact, sales_form
from django.contrib.auth.decorators import login_required

# Create your views here.

def contact_us(request):
    template="contact.html"
    if request.method == 'POST':
	    form=UserContactForm(request.POST)
	    
	    if form.is_valid():
	        form.save()
	        return redirect('index')
    else:
        form = UserContactForm
        
    context={'form':form}
        
    return render(request, template , context)


@login_required
def sales_form(request):
    """ a view that returns a submission form for a user to sell a product"""
    
    template="sales_form.html"
    if request.method == 'POST':
	    form=SalesForm(request.POST)
	    
	    if form.is_valid():
	        form.save()
	        return redirect('index')
	        
	        
    else:
        form = SalesForm
        
    context={'form':form}
        
    return render(request, template , context)

    