from web.models import SetAccountForDelete, UserAPI
import time
import datetime
from django.utils import timezone

def check_delete_account():
    get_del = SetAccountForDelete.objects.filter(delete_time__lte=timezone.now())
    print(" Accounts manually deleted:")
    for ent in get_del:
        print('  User: ', ent.user_account)
        print('   - ', ent.user_account.email)
        ent.user_account.delete()
    get_del = UserAPI.objects.filter(is_active=False, date_joined__lte=timezone.now() - datetime.timedelta(hours=24))
    print(" Not verified after 24 hours:")
    for ent in get_del:
        print('  User: ', ent)
        print('   - ', ent.email)
        ent.delete()
    print()

print("Delete job run @", timezone.now())
check_delete_account()
