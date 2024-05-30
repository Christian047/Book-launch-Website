from django.db import models
from base.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg 
# Create your models here.



class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,null=True,blank=True,default=1
    )
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reviewer')
    topic = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='user_likes')


    rating = models.IntegerField(default=0, null=True,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0),
                                ]
                                )
    
    
    class Meta:
        verbose_name_plural = 'Reviews'

    class Meta:
        ordering = ['-date_created']

    def likes_count(self):
        return self.likes.count()
  
    def average_rating(self):
        total_rating = self.book.review_set.aggregate(total=models.Sum('rating'))['total']
        review_count = self.book.review_set.count()
        if total_rating is not None and review_count > 0:
            return total_rating / review_count
        else:
            return 0

    def __str__(self):
        return f"review by {self.reviewer} for {self.book}"