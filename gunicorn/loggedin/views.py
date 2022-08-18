import json
import socket
from loggedin.network_functions import send_msg, recv_msg
from http.client import PAYMENT_REQUIRED
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from web.models import UserAPI, APICalls, UserMessages, AllUsersMessages, Payments, SetAccountForDelete
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
from loggedin.billing_dates import BillingDates
from loggedin.forms import InformationUsernameForm, PasswordUpdateForm


# Create your views here.
@login_required
def panel_dashboard(request):
    user_billing = BillingDates(request.user)
    month_start = user_billing.month_start()
    month_end = user_billing.month_end()
    day_start = user_billing.day_start()
    day_end = user_billing.day_end()

    print("Month start > " + str(day_start))
    print("Month end > " + str(day_end))
    user_calls_month = APICalls.objects.filter(user_called=request.user.id, time_called__range=[month_start, month_end], is_counted=True)
    user_calls_today = APICalls.objects.filter(user_called=request.user.id, time_called__range=[day_start, day_end], is_counted=True)
    account_type = request.user.account_type.type_name
    #account_last_call = request.user.last_api_call
    account_last_call = APICalls.objects.filter(user_called=request.user).last()
    account_messages = UserMessages.objects.filter(message_for=request.user.id, archived=False)
    all_messages = AllUsersMessages.objects.filter(archived=False)
    if account_last_call is None:
        account_last_call = 'N/A'
    else:
        account_last_call = account_last_call.time_called.strftime('%d/%m/%Y %H:%M')
    return render(request, 'loggedin/pages/index.html', {
        'api_calls': len(user_calls_month), 
        'api_calls_today': len(user_calls_today),
        'billing_month_end': month_end,
        'billing_day_end': day_end.time,
        'account_type': account_type,
        'account_last_call': account_last_call,
        'all_messages': all_messages,
        'account_messages': account_messages,
        'subscribed_until': Payments.objects.filter(payment_user=request.user.id).last(),
    })

@login_required
def panel_key(request):
    account_messages = UserMessages.objects.filter(message_for=request.user.id, archived=False)
    all_messages = AllUsersMessages.objects.filter(archived=False)
    account_success = []
    if request.method == "POST":
        if "btn_new_key" in request.POST:
            user_obj = request.user
            key = get_random_string(length=30)
            while len(UserAPI.objects.filter(api_key=key)) >= 1:
                key = get_random_string(length=30)
            user_obj.api_key = key
            user_obj.save()
            account_success.append('New key made!')
    return render(request, 'loggedin/pages/apikey.html', {
        'all_messages': all_messages,
        'account_messages': account_messages,
        'account_success': account_success,
    })

@login_required
def panel_tutorial(request):
    account_messages = UserMessages.objects.filter(message_for=request.user.id, archived=False)
    all_messages = AllUsersMessages.objects.filter(archived=False)
    return render(request, 'loggedin/pages/tutorial.html', {
        'all_messages': all_messages,
        'account_messages': account_messages,
    })

@login_required
def panel_app(request):
    return render(request, 'loggedin/pages/app.html')

@login_required
def panel_settings(request):
    account_messages = UserMessages.objects.filter(message_for=request.user.id, archived=False)
    all_messages = AllUsersMessages.objects.filter(archived=False)
    account_type = request.user.account_type.type_name
    date_joined = request.user.date_joined
    info_username_form = InformationUsernameForm({'username':request.user.username})
    password_update_form = PasswordUpdateForm
    password_errors = []
    password_success = []
    if request.method == "POST":
        #print(request.POST)
        user_obj = UserAPI.objects.filter(id=request.user.id)[0]
        info_username_form = InformationUsernameForm(request.POST)
        password_update_form = PasswordUpdateForm(request.POST)
        #if 'username' in request.POST:
            #info_username_form = InformationUsernameForm(request.POST)
        if info_username_form.is_valid():
            if info_username_form.is_valid() and (len(UserAPI.objects.filter(username=info_username_form.cleaned_data['username'])) < 1):
                user_obj.update(username=info_username_form.cleaned_data['username'])
            else:
                #Form is not valid or username is already taken
                pass
        #if 'old_password' and 'new_password' and 'new_password_confirm' in request.POST:
            #password_update_form = PasswordUpdateForm(request.POST)
        if password_update_form.is_valid():
            if (authenticate(username=user_obj.username, password=password_update_form.cleaned_data['old_password'])):
                if password_update_form.cleaned_data['new_password'] == password_update_form.cleaned_data['new_password_confirm']:
                    try:
                        user_obj.set_password(password_update_form.cleaned_data['new_password'])
                        user_obj.save()
                        password_success.append('Password Changed!')
                        update_session_auth_hash(request, user_obj)
                    except:
                        password_errors.append('Something went wrong, Please try again')
                else:
                    #print('new passwords do not match')
                    password_errors.append('New passwords do not match')
            else:
                #print('Wrong old password')
                password_errors.append('Wrong old password')
        else:
            password_errors.append('Please fill all fields')
        if 'deleteAccount' in request.POST:
            
            pass
    return render(request, 'loggedin/pages/settings.html', {
        'info_username': info_username_form,
        'password_update': password_update_form,
        'account_type': account_type,
        'date_joined': date_joined,
        'password_errors': password_errors,
        'password_success': password_success,
        'all_messages': all_messages,
        'account_messages': account_messages,
    })

@login_required
def delete_account(request):
    user_acc = request.user
    acc_del = SetAccountForDelete(user_account=user_acc)
    #UserAPI.objects.get(id=user_acc.id).active = False
    user_acc.is_active = False
    user_acc.save()
    acc_del.save()
    # Then send an Email to homeboy
    return redirect('/logout/')