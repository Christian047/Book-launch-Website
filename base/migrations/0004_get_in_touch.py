# Generated by Django 4.2.2 on 2024-05-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_review_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Get_in_touch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('customer_query', models.CharField(choices=[('Pricing Query', 'Pricing Query'), ('Author Query', 'Author Query'), ('Content Query', 'Content Query'), ('Other Query', 'Other Query')], default='Pricing Query', max_length=200)),
                ('body', models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'MODELNAME',
                'verbose_name_plural': 'MODELNAMEs',
            },
        ),
    ]
