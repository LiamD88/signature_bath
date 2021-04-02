from django.shortcuts import render
from .forms import ReviewForm
from .models import Review

def review(request):

    if request.method == 'POST':

        form = Review(    
            name = request.POST.get('name'),
            number = request.POST.get('number'),
            email = request.POST.get('email'),
            message = request.POST.get('message')
        )
        form.save()

    form = ReviewForm

    context = {
            'form': form
        }


    return render(request, 'review.html', context)
