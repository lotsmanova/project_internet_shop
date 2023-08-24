from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactListView, ProductListView, ProductCreateView, CategoryListView, \
    ProductDetailView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home_page'),
    path('contacts/', ContactListView.as_view(), name='contact_page'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/products/', ProductListView.as_view(), name='product_page'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('product_detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

]

