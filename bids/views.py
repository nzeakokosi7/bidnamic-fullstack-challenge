from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import forms


# Create your views here.
@login_required
def bid_creation(request):
    form = forms.BidCreation()
    if request.method == 'POST':
        form = forms.BidCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bid_confirmation')
    return render(request, 'bid_creation.html', context={'form': form})
