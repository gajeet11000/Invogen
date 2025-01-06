from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .token import user_tokenizer_generate

from .forms import CreateUserForm, LoginForm, UpdateUserForm

from django.conf import settings


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard')
    return render(request, 'account/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
           user = form.save()
           user.is_active = False
           user.save()
           #email verificaiton setup
           current_site = get_current_site(request)
           subject = 'Account verification email'
           message = render_to_string('account/registration/email-verification.html', {
               'user':user,
               'domain': current_site.domain,
               'uid': urlsafe_base64_encode(force_bytes(user.pk)),
               'token': user_tokenizer_generate.make_token(user)
           })
           user.email_user(subject=subject, message=message)
           send_mail("Welcome to InvoGen!", "Congratulations on creating your account", settings.DEFAULT_FROM_EMAIL, [user.email])
           return redirect('email-verification-sent')
    context = {'form':form}

    return render(request, 'account/registration/register.html', context=context)

def email_verification(request, uidb64, token):
    unique_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=unique_id)
    #success
    if user and user_tokenizer_generate.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('email-verification-success')
    else:
        return redirect('email-verification-failed')

def email_verification_sent(request):
    return render(request, 'account/registration/email-verification-sent.html')

def email_verification_success(request):
    return render(request, 'account/registration/email-verification-success.html')

def email_verification_failed(request):
    return render(request, 'account/registration/email-verification-failed.html')

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'form':form}

    return render(request, 'account/login.html', context)

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, "You were logged out securely!")
    return redirect("index")

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'account/dashboard.html')

@login_required(login_url='login')
def profile_management(request):
    form = UpdateUserForm(instance=request.user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'UserUpdateForm': form}

    return render(request, 'account/profile-management.html', context=context)

@login_required(login_url='login')
def delete_account(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.delete()
        return redirect('/')
    
    return render(request, 'account/delete-account.html')