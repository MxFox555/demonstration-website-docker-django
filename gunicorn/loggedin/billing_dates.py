from web.models import UserAPI
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone

class BillingDates():
    def __init__(self, user):
        #print(str(user.date_joined).split(".")[0].split("+")[0])
        self.user_date_made = datetime.strptime(str(user.date_joined).split(".")[0].split("+")[0], "%Y-%m-%d %H:%M:%S")

    def month_start(self, get_time=False):
        datetime_today = timezone.now()
        datetime_billing = self.user_date_made
        return_date = ""

        #print("Today > " + str(datetime_today))
        #print("Billing > " + str(datetime_billing))
        if datetime_today.day < datetime_billing.day:
            # Return the billing day with one month behind the current
            #print(datetime_billing + relativedelta(month=datetime_today.month))
            return_date = datetime_billing.replace(year=datetime_today.year) + relativedelta(month=(datetime_today.month - 1))
        elif datetime_today.day >= datetime_billing.day:
            # Return the billing day with this month
            return_date = datetime_billing.replace(year=datetime_today.year) + relativedelta(month=datetime_today.month)
        
        if get_time:
            return return_date
        else:
            return return_date
    
    def month_end(self, get_time=False):
        datetime_today = timezone.now()
        datetime_billing = self.user_date_made
        return_date = ""

        if datetime_today.day < datetime_billing.day:
            # Return the billing day with the current month
            return_date = datetime_billing.replace(year=datetime_today.year) + relativedelta(month=datetime_today.month)
        elif datetime_today.day >= datetime_billing.day:
            # Return the billing day with this day plus the next month
            return_date = datetime_billing.replace(year=datetime_today.year) + relativedelta(month=(datetime_today.month + 1))
        
        if get_time:
            return return_date
        else:
            return return_date

    def day_start(self):
        datetime_today = timezone.now()
        datetime_billing = self.user_date_made
        return_date = ""

        if datetime_today.hour < datetime_billing.hour:
            # Return the billing day with the current month
            return_date = datetime_today.replace(hour=datetime_billing.hour, minute=datetime_billing.minute, second=datetime_billing.second) - relativedelta(days=1)
        elif datetime_today.hour >= datetime_billing.hour:
            # Return the billing day with this day plus the next month
            return_date = datetime_today.replace(hour=datetime_billing.hour, minute=datetime_billing.minute, second=datetime_billing.second)

        return return_date
    
    def day_end(self):
        datetime_today = timezone.now()
        datetime_billing = self.user_date_made
        return_date = ""

        if datetime_today.hour < datetime_billing.hour:
            # Return the billing day with the current month
            return_date = datetime_today.replace(hour=datetime_billing.hour, minute=datetime_billing.minute, second=datetime_billing.second)
        elif datetime_today.hour >= datetime_billing.hour:
            # Return the billing day with this day plus the next month
            return_date = datetime_today.replace(hour=datetime_billing.hour, minute=datetime_billing.minute, second=datetime_billing.second) + relativedelta(days=1)

        return return_date


    