from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from vendor.forms import VendorCreationForm, ProductsAdd
from vendor.models import VendorProfile, Product, Category
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.views import generic
from django.core.paginator import Paginator
from ASE1.decorators import vendor_required


def home(request):
    return HttpResponse('Dear vendor, Welcome to the home page!')


def index(request):
    return render(request, 'vendor/base.html')


class ItemsView(generic.DetailView):
    template_name = 'customer/items.html'
    model = Category
    context_object_name = 'cat'


class IndexView(generic.ListView):
    template_name = 'customer/index.html'
    context_object_name = 'cat'

    def get_queryset(self):
        return Category.objects.all()


@login_required(login_url='vendor:login')
@vendor_required
def add_products(request):
    if request.method == 'POST':
        form = ProductsAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor:view_products')

    else:
        form = ProductsAdd()
    return render(request, 'vendor/add_products.html', {'form': form})


@login_required(login_url='vendor:login')
@vendor_required
def view_products(request):
    product_list = Product.objects.all().order_by('prod_name')

    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'vendor/view_products.html', {'products': products})


@login_required(login_url='vendor:login')
@vendor_required
def modify_products(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST['prod_name']
        cat = request.POST['prod_cat']
        brand = request.POST['prod_brand']
        qty = request.POST['prod_qty']
        cost = request.POST['prod_cost']

        product.prod_name = name
        product.qty = qty
        product.cost = cost
        product.category.cat_name = cat
        product.brand = brand
        product.save()
        return redirect('vendor:view_products')

    return render(request, 'vendor/modify_product.html', {'product': product})


@login_required(login_url='vendor:login')
@vendor_required
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    name = product.prod_name
    product.delete()
    return render(request, 'vendor/deleted.html', {'name': name})

###########   EARLIER   ##########################################
# def vendor_signup(request):
#     if request.method == 'POST':
#         form = VendorCreationForm(request.POST)
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
###########   EARLIER   ##########################################

###########   EARLIER   ##########################################
# def vendor_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect('vendor:view_products')
#     else:
#         form = AuthenticationForm
#     return render(request, 'vendor/login.html', {'form': form})
###########   EARLIER   ##########################################

###########   EARLIER   ##########################################
# def vendor_logout(request):
#     logout(request)
#     return render(request, 'vendor/logout.html')
###########   EARLIER   ##########################################
