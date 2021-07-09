from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'orders'

# router = routers.DefaultRouter()
# router.register('order', views.OrdersView.as_view())

urlpatterns = [
    path('order/', views.OrdersView.as_view()),
]
