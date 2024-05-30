from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('addproduct/', AddProduct.as_view(), name='addproduct'),
    path('getprice/', GetPricingList.as_view(), name='addproduct'),
]