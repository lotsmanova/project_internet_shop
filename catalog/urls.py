from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactListView, ProductListView, ProductCreateView, CategoryListView, \
    BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home_page'),
    path('contacts/', ContactListView.as_view(), name='contact_page'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/products/', ProductListView.as_view(), name='product_page'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),

]

