# Generated by Django 2.2.2 on 2019-07-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laundry', '0007_auto_20190720_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='laundry',
            name='delivery_flat',
            field=models.TextField(default=' ', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laundry',
            name='delivery_locality',
            field=models.TextField(default=' ', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laundry',
            name='delivery_pincode',
            field=models.TextField(default=' ', max_length=500),
            preserve_default=False,
        ),
    ]