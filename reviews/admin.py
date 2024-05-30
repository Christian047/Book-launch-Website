from django.contrib import admin

# Register your models here.
from reviews.models import *

@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ('reviewer', 'book','topic', 'date_created' ,'rating')

    