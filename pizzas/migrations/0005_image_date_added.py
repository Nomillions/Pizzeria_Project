# Generated by Django 3.2 on 2021-05-03 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
