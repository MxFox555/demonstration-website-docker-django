# Generated by Django 4.0.5 on 2022-06-09 09:20

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_alter_admincontactmessage_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admincontactmessage',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='allusersmessages',
            name='message_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='apicalls',
            name='time_called',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 9, 9, 20, 21, 346353, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='resetemailentry',
            name='time_made',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_click_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='setaccountfordelete',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 9, 20, 21, 346041, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='message_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
