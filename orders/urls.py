from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.AddProductView.as_view(), name='product'),
    path('product/order/', views.OrderProductView.as_view(), name='product_order')
]