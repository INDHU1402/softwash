# Generated by Django 2.2.2 on 2019-07-25 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Laundry', '0014_auto_20190725_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laundry',
            name='delivery_city',
        ),
        migrations.RemoveField(
            model_name='laundry',
            name='pickup_city',
        ),
    ]
