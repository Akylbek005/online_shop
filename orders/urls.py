from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.OrdersView.as_view())
]
