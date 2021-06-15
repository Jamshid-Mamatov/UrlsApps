from django.urls import path
from .views import home,customer,product

urlpatterns=[
    path('',home),
    path('customer/',customer),
    path('product/',product),
]