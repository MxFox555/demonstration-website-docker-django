import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model

# Create your models here.
class AccountType(models.Model):
    type_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'account_types'

class UserAPI(AbstractUser):
    email = models.EmailField(unique=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.PROTECT, null=True)
    #last_api_call = models.DateTimeField(null=True)
    api_key = models.CharField(max_length=30, unique=True, null=True)
    activate_key = models.CharField(max_length=100, unique=True, null=True)

    REQUIRED_FIELDS = ["email", "password"]

    class Meta:
        db_table = 'users'

class APICalls(models.Model):
    user_called = models.ForeignKey(UserAPI, on_delete=models.SET_NULL, null=True)
    time_called = models.DateTimeField(default=timezone.now)
    is_counted = models.BooleanField(default=True)

    class Meta:
        db_table = 'api_calls'

class UserMessages(models.Model):
    message_for = models.ForeignKey(UserAPI, on_delete=models.SET_NULL, null=True)
    message_date = models.DateTimeField(default=timezone.now)
    message_title = models.CharField(max_length=50, default='title')
    message_content = models.CharField(max_length=300, default='message')
    archived = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_messages'

class AllUsersMessages(models.Model):
    message_date = models.DateTimeField(default=timezone.now)
    message_title = models.CharField(max_length=50, default='title')
    message_content = models.CharField(max_length=300, default='message')
    archived = models.BooleanField(default=False)

    class Meta:
        db_table = 'all_user_messages'

class SetAccountForDelete(models.Model):
    user_account = models.ForeignKey(UserAPI, on_delete=models.CASCADE)
    delete_click_time = models.DateTimeField(default=timezone.now)
    delete_time = models.DateTimeField(default=timezone.now() + relativedelta(hours=24))

    class Meta:
        db_table = 'account_delete'

class Payments(models.Model):
    payment_user = models.ForeignKey(UserAPI, on_delete=models.SET_NULL, null=True)
    payment_email = UserAPI.email
    payment_date = models.DateTimeField(default=timezone.now)
    payment_expiry = models.DateTimeField(default=timezone.now() + relativedelta(months=1), null=False)
    payment_amount = models.DecimalField(decimal_places=2, max_digits=100)
    account_type_for = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    #stripe_info =

class AdminContactMessage(models.Model):
    contact_email = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    time = models.DateTimeField(default=timezone.now)

class ResetEmailEntry(models.Model):
    reset_account = models.ForeignKey(UserAPI, on_delete=models.CASCADE)
    reset_key = models.CharField(max_length=100, unique=True)
    time_made = models.DateTimeField(default=timezone.now)
    redeemed = models.BooleanField(default=False)