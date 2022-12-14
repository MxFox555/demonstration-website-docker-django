# Generated by Django 4.0.4 on 2022-05-30 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_userapi_activate_key_alter_admincontactmessage_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admincontactmessage',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 19, 58, 38, 620550)),
        ),
        migrations.AlterField(
            model_name='allusersmessages',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 19, 58, 38, 620049)),
        ),
        migrations.AlterField(
            model_name='apicalls',
            name='time_called',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 19, 58, 38, 619550)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 19, 58, 38, 620550)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 30, 19, 58, 38, 620550)),
        ),
        migrations.AlterField(
            model_name='resetemailentry',
            name='time_made',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 19, 58, 38, 621050)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_click_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 19, 58, 38, 620049)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 19, 58, 38, 620049)),
        ),
        migrations.AlterField(
            model_name='userapi',
            name='activate_key',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 19, 58, 38, 619550)),
        ),
    ]
