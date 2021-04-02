from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

def contact(request):

    if request.method == 'POST':

        form = Contact(    
            name = request.POST.get('name'),
            number = request.POST.get('number'),
            email = request.POST.get('email'),
            message = request.POST.get('message')
        )
        form.save()

    form = ContactForm

    context = {
            'form': form
        }

    return render(request, 'contact.html', context)