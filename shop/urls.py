from django.urls import path
from .views import (
    HomePageView, 
    ProductDetailView, 
    AllProductsView,
    CartView,
    OrderSuccessView,
    OrderView
)


app_name = 'shop'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('all/', AllProductsView.as_view(), name='all'),
    
    # Product Detail 
    path('detail/', ProductDetailView.as_view(), name='detail'),
    
    # Cart Page
    path('cart/', CartView.as_view(), name='cart'),
    
    # Order success
    path('order-success', OrderSuccessView.as_view(), name='order_succes'),
    
    # Order success
    path('order/', OrderView.as_view(), name='order')
]   
