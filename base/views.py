
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from reviews.models import *
from base.context_generator import *



class Home(View):
    def get(self, request):
        review = Review.objects.all()
        average_rating = Review.objects.aggregate(Avg('rating'))['rating__avg']
        prices = PricingPlan.objects.all()
        common_context = get_common_context()

        total_reviews = review.count()


        if average_rating is None:
            average_rating = 0

        # Calculate the number of full stars
        full_stars = int(average_rating)

        # Calculate the fractional part
        fractional_part = average_rating - full_stars

        # Determine if there is a quarter star
        quarter_star = 1 if 0.25 <= fractional_part < 0.5 else 0

        # Determine if there is a half star
        half_star = 1 if fractional_part >= 0.5 else 0

        # Number of empty stars
        empty_stars = 5 - full_stars - half_star - quarter_star

        context = {
            **common_context,
            'average_rating': average_rating,
            'full_stars': full_stars,
            'half_star': half_star,
            'quarter_star': quarter_star,
            'prices': prices,
            'empty_stars': empty_stars,
            'total_reviews': total_reviews,
        }
        return render(request, 'base/index1.html', context)



class AddProduct(View):
    def get(self, request):
        return render(request, 'base/product_form.html')
        

class GetPricingList(View):
    def get(self, request):
        prices = PricingPlan.objects.all()
        context = get_common_context()
        return render(request, 'base/price.html',context)

