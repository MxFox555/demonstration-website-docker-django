from django.contrib import admin
from django.contrib.auth.models import User
from web.models import UserAPI, AdminContactMessage, UserMessages, AllUsersMessages, AccountType, APICalls, Payments, SetAccountForDelete, ResetEmailEntry

# Register your models here.
admin.site.register(APICalls)
admin.site.register(UserAPI)
admin.site.register(AdminContactMessage)
admin.site.register(UserMessages)
admin.site.register(AccountType)
admin.site.register(Payments)
admin.site.register(SetAccountForDelete)
admin.site.register(ResetEmailEntry)
admin.site.register(AllUsersMessages)