from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from .forms import ContactForm

def contact(request):

    if request.method == 'POST':

        form = Contact(    
            name = request.POST.get('name'),
            message = request.POST.get('message'),
            email = request.POST.get('email')
        )
        form.save()

    form = ContactForm

    context = {
            'form': form
        }

    return render(request, 'contact.html', context)