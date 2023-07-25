from django.shortcuts import render

def home_page(request):
    return render(request, 'catalog/home_page.html')

def contact_page(request):
    return render(request, 'catalog/contact_page.html')
