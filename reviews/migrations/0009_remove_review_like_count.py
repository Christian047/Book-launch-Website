# Generated by Django 5.0.6 on 2024-05-17 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_review_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='like_count',
        ),
    ]
