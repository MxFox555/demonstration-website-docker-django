# Generated by Django 4.0.5 on 2022-06-10 00:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_alter_payments_payment_expiry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 10, 0, 18, 9, 910016, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 0, 18, 9, 909693, tzinfo=utc)),
        ),
    ]
