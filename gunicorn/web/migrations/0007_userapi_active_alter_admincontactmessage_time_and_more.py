# Generated by Django 4.0.4 on 2022-05-29 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_remove_payments_premium_account_expiry_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapi',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='admincontactmessage',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 15, 41, 45, 760235)),
        ),
        migrations.AlterField(
            model_name='apicalls',
            name='time_called',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 15, 41, 45, 759235)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 15, 41, 45, 760235)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 15, 41, 45, 760235)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_click_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 15, 41, 45, 759735)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 15, 41, 45, 759735)),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 15, 41, 45, 759735)),
        ),
    ]
