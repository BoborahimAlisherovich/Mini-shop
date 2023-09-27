from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import UpdateView , DeleteView

class HomePageView(TemplateView):
    template_name = 'index.html'
    
class ProductDetailView(TemplateView):
    template_name = 'product.html'

class AllProductsView(TemplateView):
    template_name = 'all-products.html'
    
class CartView(TemplateView):
    template_name = 'cart-page.html'

class OrderSuccessView(TemplateView):
    template_name = 'order-success.html'

class OrderView(TemplateView):
    template_name = 'order.html'