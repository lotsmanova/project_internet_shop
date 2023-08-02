from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactListView, ProductListView, ProductCreateView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home_page'),
    path('contacts/', ContactListView.as_view(), name='contact_page'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/products/', ProductListView.as_view(), name='product_page'),
    path('add_product/', ProductCreateView.as_view(), name='add_product')
]

