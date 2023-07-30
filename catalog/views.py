from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from catalog.form import ProductForm
from catalog.models import Product, Contact, Category


def home_page(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    latest_products = Product.objects.order_by('-date_create')[:5]
    for product in latest_products:
        print(product.name, product.price)

    context = {
        'object_list': page_obj,
        'title': 'Главная',
        'page_obj': page_obj
    }
    return render(request, 'catalog/home_page.html', context)


def contact_page(request):
    context = {
        'contacts': Contact.objects.all(),
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact_page.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
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


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:home_page')
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})