from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Review, Like


@require_POST
def like_review(request):
    review_id = request.POST.get('review_id')
    review = get_object_or_404(Review, pk=review_id)
    
    if request.user.is_authenticated:
        like, created = Like.objects.get_or_create(user=request.user, review=review)
        if created:
            review.likes_count += 1
            review.save()
            liked = True
        else:
            if review.likes_count == 0:
                review.likes_count = 1
                review.save()
                liked = True
            else:
                review.like_count = 0
                like.delete()
                review.save()
                liked = False

        return JsonResponse({'like_count': review.like_count, 'liked': liked})
    else:
        # Just return the like count without making changes
        return JsonResponse({'like_count': review.like_count, 'error': 'Authentication required.'}, status=401)