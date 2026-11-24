
from django.shortcuts import render

def home(request):
    return render(request, 'restaurant/home.html')
def menu(request):
    return render(request, 'restaurant/menu.html')
def administration(request):
    return render(request, 'restaurant/administration.html')
def contact(request):
    return render(request, 'restaurant/contact.html')