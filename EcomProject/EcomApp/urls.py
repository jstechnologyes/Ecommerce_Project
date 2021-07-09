
from django.urls import path
from .views import Home, product_single



urlpatterns = [
      path('', Home, name='home'),
      path('product/<id>', product_single, name='product-single'),
]