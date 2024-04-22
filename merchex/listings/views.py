from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listings


def hello(request):
    bands = Band.objects.all()
    return render(request,
    'listings/hello.html',
    {'bands': bands})

def about(request):
    return render(request,
    'listings/about.html')

def contact(request):
    return render(request,
    'listings/contact.html')

def listings(request):
    listings = Listings.objects.all()
    return render(request,
    'listings/listings.html',
    {'listings': listings})
