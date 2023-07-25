from django.urls import path

from catalog.views import home_page, contact_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('templates/', contact_page, name='contact_page'),
]

