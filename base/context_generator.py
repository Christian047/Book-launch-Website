# context_generators.py
from base.models import *
from reviews.models import *

def get_common_context():
    review = Review.objects.all()
    prices = PricingPlan.objects.all()
    context = {
        'review': review,
        'prices': prices,
        
    }
    return context
