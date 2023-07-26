from django.shortcuts import render

from catalog.models import Product, Contact


def home_page(request):
    latest_products = Product.objects.order_by('-date_create')[:5]
    for product in latest_products:
        print(product.name, product.price)
        context = {
            'latest_products': latest_products,
        }
    return render(request, 'catalog/home_page.html', context)


def contact_page(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, 'catalog/contact_page.html', context)
