# Generated by Django 2.2.2 on 2019-07-14 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Laundry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laundry',
            old_name='delivery_address',
            new_name='delivery_date',
        ),
        migrations.RenameField(
            model_name='laundry',
            old_name='pickup_address',
            new_name='pickup_date',
        ),
    ]
