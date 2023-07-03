# Generated by Django 3.2.9 on 2023-07-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20211220_1532'),
        ('bookstore', '0009_auto_20230701_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='book_category', to='category.Category'),
        ),
    ]