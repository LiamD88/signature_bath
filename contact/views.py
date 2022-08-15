from django.forms.widgets import NumberInput
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact
import os



def contact(request):



    return render(request, 'contact.html')