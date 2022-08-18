# Generated by Django 4.0.4 on 2022-06-01 23:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_remove_userapi_last_api_call_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apicalls',
            name='is_counted',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='admincontactmessage',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 9, 14, 33, 738054)),
        ),
        migrations.AlterField(
            model_name='allusersmessages',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 9, 14, 33, 737554)),
        ),
        migrations.AlterField(
            model_name='apicalls',
            name='time_called',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 9, 14, 33, 737054)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 9, 14, 33, 738054)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 2, 9, 14, 33, 738054)),
        ),
        migrations.AlterField(
            model_name='resetemailentry',
            name='time_made',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 9, 14, 33, 738554)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_click_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 9, 14, 33, 737554)),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 9, 14, 33, 737554)),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 9, 14, 33, 737054)),
        ),
    ]