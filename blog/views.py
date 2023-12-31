from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.templatetags.pytils_translit import slugify

from blog.forms import BlogForm
from blog.models import Blog
from blog.services import blog_send_mail


class BlogCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания"""

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            new_net = form.save()
            new_net.slug = slugify(new_net.head)
            new_net.save()
        return super().form_valid(form)


class BlogListView(ListView):
    """Контроллер общего просмотра"""

    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_public=True)
        return queryset


class BlogDetailView(DetailView):
    """Контроллер просмотра записи"""

    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        if self.object.count_views == 100:
            blog_send_mail(self.object)
        return self.object


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер редактирования"""
    model = Blog
    form_class = BlogForm
    login_url = reverse_lazy('users:login')


    def form_valid(self, form):
        if form.is_valid():
            new_net = form.save()
            new_net.slug = slugify(new_net.head)
            new_net.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления"""
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    login_url = reverse_lazy('users:login')

