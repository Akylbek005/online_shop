from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.AddProductAPIView.as_view(), name='product'),
]
