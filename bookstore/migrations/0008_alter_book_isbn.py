# Generated by Django 3.2.9 on 2023-06-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, default='5911696758734', max_length=13, null=True, unique=True),
        ),
    ]
