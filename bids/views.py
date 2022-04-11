from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import forms
from . import models


# Create your views here.
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = forms.BidCreation(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.bidder = request.user
            temp_form.save()
            return redirect('home')
    bids = models.Bid.objects.all()
    bid_list = list(bids)
    return render(request, 'dashboard.html', {'bids': bid_list})

