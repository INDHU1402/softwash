# Generated by Django 2.2.2 on 2019-07-19 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Laundry', '0005_cartvalue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartvalue',
            old_name='total',
            new_name='bill_amount',
        ),
    ]
