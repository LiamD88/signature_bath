from django.forms.widgets import NumberInput
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact
import os



def contact(request):

    if request.method == 'POST':

        form = Contact(    
            name = request.POST.get('name'),
            number = request.POST.get('number'),
            email = request.POST.get('email'),
            message = request.POST.get('message')
            
        ) 
        form.save()
                      

        send_mail(
            'new email',
            'new email',
            os.environ.get('EMAIL'),
            ['signaturebathrooms.88@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for your message, we will be in touch as soon as we can!')
        return redirect('home')

    else:

        form = ContactForm

    context = {
            'form': form
        }


    return render(request, 'contact.html')