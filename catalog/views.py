from django.shortcuts import render

from catalog.models import Product, Contact, Category


def home_page(request):
    latest_products = Product.objects.order_by('-date_create')[:5]
    for product in latest_products:
        print(product.name, product.price)
        context = {
            'object_list': latest_products,
            'title': 'Главная'
        }
    return render(request, 'catalog/home_page.html', context)


def contact_page(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact_page.html', context)


def categories(request):
    categories = Category.objects.all()
    context = {
        'object_list': categories,
        'title': 'Категории'
    }
    return render(request, 'catalog/categories.html', context)


def product_page(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{category_item.name}'
    }
    return render(request, 'catalog/product_page.html', context)
