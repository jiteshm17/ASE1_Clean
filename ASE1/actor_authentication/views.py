from datetime import datetime
from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .forms import UserCreationForm
from customer.models import CustomerProfile
from vendor.models import VendorProfile
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
###########   EARLIER   ########################
# def customer_signup(request):
#     if request.method == 'POST':
#         form = CustomerCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             contact_number = form.cleaned_data['contact_number']
#             c = CustomerProfile.objects.get(Customer=user)
#             # send_mail('Hello Customer', 'Thanks for registering', settings.EMAIL_HOST_USER, [user.email],
#             #           fail_silently=True)
#             c.phone_number = contact_number
#             login(request, user)
#             return redirect('customer:home')
#     else:
#         form = CustomerCreationForm()
#     return render(request, 'customer/signup.html', {'form': form})
###########   EARLIER   ########################

def customer_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect(reverse('customer:actor_authentication:login_all'))
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'customer/signup.html', context)


###########   EARLIER   ########################
# def vendor_signup(request):
#     if request.method == 'POST':
#         form = VendorCreationForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             contact_number = form.cleaned_data['contact_number']
#             # new_vendor = VendorProfile(Vendor=user,phone_number=contact_number)
#             VendorProfile.objects.create(Vendor=user, phone_number=contact_number)
#             # send_mail('Hello vendor', 'Thanks for registering', settings.EMAIL_HOST_USER, [user.email],
#             #           fail_silently=True)
#             login(request, user)
#             return redirect('vendor:view_products')
#     else:
#         form = VendorCreationForm()
#     return render(request, 'vendor/signup.html', {'form': form})
###########   EARLIER   ########################

def vendor_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            VendorProfile.objects.create(Vendor=user)
            return redirect('vendor:actor_authentication:login_all')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'vendor/signup.html', context)


def login_all(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('customer:home')
    else:
        form = AuthenticationForm
    return render(request, 'customer/login.html', {'form': form})


@login_required
def logout_all(request):
    logout(request)
    return render(request, 'customer/logout.html')


def signup_all(request):
    return render(request, 'actor_authentication/signup_all.html')