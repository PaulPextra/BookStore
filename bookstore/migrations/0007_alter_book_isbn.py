# Generated by Django 3.2.9 on 2023-06-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_auto_20211220_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, default='3012991520314', max_length=13, null=True, unique=True),
        ),
    ]
