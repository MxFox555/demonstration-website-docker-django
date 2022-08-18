# Generated by Django 4.0.5 on 2022-06-30 22:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0098_alter_payments_payment_expiry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 30, 22, 56, 27, 788066, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 1, 22, 56, 27, 787732, tzinfo=utc)),
        ),
    ]
