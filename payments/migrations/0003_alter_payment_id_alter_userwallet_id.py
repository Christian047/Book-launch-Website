# Generated by Django 5.0.4 on 2024-05-08 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_userwallet_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userwallet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
