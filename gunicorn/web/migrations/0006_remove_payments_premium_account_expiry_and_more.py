# Generated by Django 4.0.4 on 2022-05-25 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_payments_payment_expiry_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='premium_account_expiry',
        ),
        migrations.AlterField(
            model_name='admincontactmessage',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 25, 20, 11, 39, 267654)),
        ),
        migrations.AlterField(
            model_name='apicalls',
            name='time_called',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 25, 20, 11, 39, 266655)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 25, 20, 11, 39, 267155)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 25, 20, 11, 39, 267155)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_click_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 25, 20, 11, 39, 267155)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 20, 11, 39, 267155)),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 25, 20, 11, 39, 266655)),
        ),
    ]
