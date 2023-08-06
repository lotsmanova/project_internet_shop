from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.templatetags.pytils_translit import slugify
from catalog.form import ProductForm, BlogForm
from catalog.models import Product, Contact, Category, Blog



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


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_net = form.save()
            new_net.slug = slugify(new_net.head)
            new_net.save()
        return super().form_valid(form)   


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_public=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        if self.object.count_views == 100:
            send_mail(
                'Поздравляем!',
                f'Ваша статья "{self.object.head}" набрала 100 просмотров!',
                settings.EMAIL_HOST_USER,
                ['lotsmanovavioletta@yandex.ru'],
                fail_silently=False,
            )
        return self.object



class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    # success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_net = form.save()
            new_net.slug = slugify(new_net.head)
            new_net.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
