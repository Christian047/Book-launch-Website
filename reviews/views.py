from django.shortcuts import render,redirect
from django.views import View
from base.models import *
from reviews.models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin




# Review for object
class AddReview(LoginRequiredMixin,View):
    login_url = '/auth/login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'You need to be logged in to add a review.')
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        review= Review.objects.all()
        context = {
            'review': review,               
        }
        return render(request,'reviews/add_reviews.html', context)
    
    def post(self, request):
        rating = request.POST.get('rating')
        body = request.POST.get('body')
        topic = request.POST.get('topic')
        
        if not rating or not body:
            messages.error(request,'fill out the form')
        try:

            book = Book.objects.get(id=1)
            Review.objects.create (
                reviewer=request.user,
                body= body,
                book= book,
                topic= topic,
                rating= rating
            )
            messages.success(request,'Review created successfully')
            return redirect('home')

        except Exception as e:

            messages.error(request,  f'something went wrong: {e}')
            return render(request, 'reviews/add_reviews.html')
            




class UpdateReview(View,LoginRequiredMixin):
    def get(self,request,pk):
        obj= Review.objects.get(pk=pk)
        context = {
            'obj': obj,               
        }
        return render(request,'reviews/update_review.html', context)
    
    def post(self,request,pk):
        rating = request.POST.get('rating')
        body = request.POST.get('body')
        topic = request.POST.get('topic')
        
        if not rating or not body:
            messages.error(request,'fill out the form')
        try:

            obj= Review.objects.get(pk=pk)
            obj.save(
            )
            messages.success(request,'Review updated successfully')
            return redirect('home')

        except Exception as e:

            messages.error(request,  f'something went wrong: {e}')
            return render(request, 'reviews/add_reviews.html')
            



class Show_Review(View):
    def get(self, request, *args, **kwargs):
        review = Review.objects.all()
        context = {'review': review}
        return render(request, 'reviews/show_review.html', context)
    
    def post(self, request, *args, **kwargs):
        pass







class DeleteReview(View,LoginRequiredMixin):
    def get(self,request,pk):
        obj= Review.objects.get(pk=pk)
        context = {
            'obj': obj,               
        }
        return render(request,'reviews/delete_reviews.html', context)
    def post(self,request,pk):
        review= Review.objects.get(pk=pk)
        review.delete()
        messages.success(request,'Review deleted')
        return redirect('home')


