from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from catalog.form import ProductForm
from catalog.models import Product, Contact, Category


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home_list.html'
    paginate_by = 4


    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        latest_products = Product.objects.order_by('-date_create')[:5]
        context_data['latest_products'] = latest_products

        return context_data


class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        pk = self.kwargs.get('pk')
        category_item = Category.objects.get(pk=pk)
        context_data['title'] = f'{category_item.name}'
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home_page')
