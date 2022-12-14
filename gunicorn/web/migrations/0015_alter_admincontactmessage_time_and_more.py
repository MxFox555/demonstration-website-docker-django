# Generated by Django 4.0.5 on 2022-06-08 02:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_resetemailentry_redeemed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admincontactmessage',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 2, 6, 27, 63089)),
        ),
        migrations.AlterField(
            model_name='allusersmessages',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 2, 6, 27, 62019)),
        ),
        migrations.AlterField(
            model_name='apicalls',
            name='time_called',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 2, 6, 27, 61379)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 2, 6, 27, 62675)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 8, 2, 6, 27, 62688)),
        ),
        migrations.AlterField(
            model_name='resetemailentry',
            name='time_made',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 2, 6, 27, 63332)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_click_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 2, 6, 27, 62354)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 2, 6, 27, 62367)),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 2, 6, 27, 61697)),
        ),
    ]
