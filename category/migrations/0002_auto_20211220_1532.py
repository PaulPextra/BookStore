# Generated by Django 3.2.9 on 2021-12-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
