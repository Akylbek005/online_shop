from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'products'

router = routers.DefaultRouter()
router.register('product', views.ProductView)

urlpatterns = [
    path('', include(router.urls)),
]
