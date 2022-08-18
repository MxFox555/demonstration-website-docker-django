from smtplib import SMTPException
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from web.models import UserAPI, ResetEmailEntry, APICalls
from web.forms import LoginForm, SignupForm, ForgotPasswordForm, ResetPasswordWithKey
from ratelimit.decorators import ratelimit

# Create your views here.
def landing(request):
    return render(request, 'web/index.html')

def pricing(request):
    return render(request, 'web/features.html')

def contact(request):
    return render(request, 'web/contact.html')

def privacypolicy(request):
    return render(request, 'web/privacypolicy.html')

def termsofservice(request):
    return render(request, 'web/termsofservice.html')

def signup(request):
    #If method is POST
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Account activation'
            html_message = render_to_string('web/message_page.html', {
                'message_title': subject,
                'message_body': 'Follow <a href="https://stockinterestmetric.com/activate/' + str(UserAPI.objects.get(email=form.cleaned_data.get("email")).activate_key) + '">this link</a> to activate your account with Stock Interest Metric',
            })
            plain_message = strip_tags(html_message)
            from_email = 'Stock Interest Metric <stockinterestmetric@gmail.com>'
            to = str(form.cleaned_data.get("email"))
            send_mail(
                subject,
                plain_message,
                from_email,
                [to],
                html_message=html_message,
                fail_silently=True,
            )
            return render(request, 'web/signup_success.html')
        else:
            msg_errors = str(form.errors).split("<li>")
            return render(request, 'web/signup.html', {'signup_form': form, 'error_message': form.errors})
    else:
        form = SignupForm

    return render(request, 'web/signup.html', {'signup_form': form})

@ratelimit(key='post:username')
def pagelogin(request):
    error_messages = []
    form = LoginForm
    if request.user.is_authenticated:
        return redirect('/panel/home/')
    if request.method == 'POST':
        #form = LoginForm(request.POST)
        login_info = request.POST
        user = authenticate(username=login_info['username'], password=login_info['password'])
        if user is not None:
            user_obj = UserAPI.objects.get(username=login_info['username'])
            if not user_obj.is_active:
                user_obj.is_active = True
                user_obj.save()
            login(request, user)
            return redirect('/panel/home/')
        else:
            form = LoginForm(request.POST)
            error_messages.append("Username or password is incorrect")

    return render(request, 'web/login.html', {'login_form': form, 'error_messages': error_messages})

def pagelogout(request):
    logout(request)
    return redirect('/login/')

def pageforgotpassword(request):
    forgot_form = ForgotPasswordForm
    error_message = []
    if request.method == "POST":
        forgot_form = ForgotPasswordForm(request.POST)
        if forgot_form.is_valid():
            user_obj = UserAPI.objects.filter(email=forgot_form.cleaned_data.get("email"))
            if user_obj.exists() and user_obj[0].is_active:
                key = get_random_string(length=100)
                while len(ResetEmailEntry.objects.filter(reset_key=key)) >= 1:
                    key = get_random_string(length=100)
                
                change_obj = ResetEmailEntry(reset_account=user_obj[0], reset_key=key)
                change_obj.save()
                #Send reset email
                subject = 'Password reset'
                html_message = render_to_string('web/message_page.html', {
                    'message_title': subject,
                    'message_body': 'Follow <a href="https://stockinterestmetric.com/resetpassword/' + str(key) + '">this link</a> to reset your password with Stock Interest Metric',
                })
                plain_message = strip_tags(html_message)
                from_email = 'Stock Interest Metric <stockinterestmetric@gmail.com>'
                to = str(user_obj[0].email)
                send_mail(
                    subject,
                    plain_message,
                    from_email,
                    [to],
                    html_message=html_message,
                    fail_silently=True,
                )
                #Go to success page
                return render(request, 'web/reset_email_success.html')
            else:
                #Email does not exist
                error_message.append("Email is not associated with any account. (Account also may need activation)")
        else:
            #Email is not valid
            error_message.append("Email is not in valid format")
    return render(request, 'web/reset_email.html', {
        'email_form': forgot_form,
        'error_message': error_message,
    })

def pageresetpassword(request, key):
    error_messages = []
    password_success = []
    if request.method == "POST":
        reset_pwd_form = ResetPasswordWithKey(request.POST)
        entry = ResetEmailEntry.objects.get(reset_key=request.POST["key"])
        user = entry.reset_account
        if reset_pwd_form.is_valid():
            if reset_pwd_form.cleaned_data['new_password'] == reset_pwd_form.cleaned_data['new_password_confirm']:
                try:
                    user.set_password(reset_pwd_form.cleaned_data['new_password'])
                    user.save()
                    entry.redeemed = True
                    entry.save()
                    password_success.append('Password Changed!')
                    return render(request, 'web/acc_success.html', {'password_change_success': password_success})
                except:
                    error_messages.append('Something went wrong, Please try again')
            else:
                #print('Wrong old password')
                error_messages.append('Key does not exist')
        else:
            print(reset_pwd_form.errors)
            error_messages.append('Please fill all fields')
    
    reset_pwd_form = ResetPasswordWithKey

    return render(request, 'web/reset_password.html', {
        'reset_password': reset_pwd_form,
        'key': key,
        'error_messages': error_messages,
    })

def pageactivate(request, key):
    user_obj = UserAPI.objects.filter(activate_key=key)
    if user_obj.exists():
        user_obj = UserAPI.objects.get(activate_key=key)
        user_obj.is_active = True
        user_obj.save()
        return render(request, 'web/acc_success.html', {'password_change_success': ['Account was successfully activated!']})
    else:
        return render(request, 'web/message_page.html', {
            'message_title': 'Key not found',
            'message_body': 'The account for this key does not exist'
        })
