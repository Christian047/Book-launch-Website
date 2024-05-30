from django.urls import path
from .views import *

urlpatterns = [
    path('', AddReview.as_view(), name='review'),
    path('delete/<int:pk>', DeleteReview.as_view(), name='delete_review'),
    path('update/<int:pk>', UpdateReview.as_view(), name='update_review'),
    path('show_review/', Show_Review.as_view(), name='show_review'),
]
