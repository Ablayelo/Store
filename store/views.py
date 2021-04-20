from profiles.models import Profile
from django.contrib.auth.models import User
from django.core import exceptions
from django.db.models.expressions import Exists
from .forms import LoginForm, SignUpForm
from django.core.checks import messages
from store.models import Category, Order, OrderItem, Product
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# ============================And of importspro=========================


# =================Login View========================================
# def login_view(request):
#     if request.user.is_authenticated:
#         logout(request)
#     form = LoginForm(request.POST)
#     if request.method == 'POST':
#         username = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, username = username, password = password)
#         #user = User.objects.get(username = username)
#         if user is not None:
#             login(request, user)
#             return redirect('store:index')
#     return render(request, 'store/login.html')
def loginView(request):
    form = LoginForm(request.POST)
    msg = None
    if not request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                profile = authenticate(username=username, password=password)
                if profile is not None:
                    login(request, profile)
                    return redirect('profile:profile')
                else:
                        msg = 'Infos invalides'

            else:
                msg = 'Vérifier vos informtions'
    else:
        return redirect('store:index')

    return render(request, 'store/login.html', {'form': form, 'msg': msg})


# ==============================SingUp====================================
def registerUser(request):

    msg = None
    success = False

    if request.method == "POST":
        
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #msg = 'Compte crée avec succés  <a href="/login">Se connecter</a>.'
            success = True
            return redirect('store:index')
        else:
            msg = 'Formulaire invalide'
    else:
        form = SignUpForm()

    return render(request, "store/register.html", {"form": form, "msg": msg, "success": success})

# ===================Logout================================================


# =========================Home Page view============================


def index(request):

    # affiche tous les produits sur la page d'accueil
    if request.user.is_authenticated:
        return redirect('profile:profile')
    else:
        products = Product.objects.all()
        context = {'products': products}
    return render(request, 'store/index.html', context)

# =========================Peoduct Detail view===============


def productDetail(request, id):
    product = Product.objects.get(id=id)

    context = {'product': product, }
    return render(request, 'store/product-detail.html', context)

# ========================Cart view===========================


def cart(request):
    
    user = Profile.objects.filter(first_nane=request.user.first_name, last_name=request.user.last_name)
    profile = request.user
    order = Order.objects.filter(profile=profile)
    if order:  
        if request.user.is_authenticated:
            order, created = Order.objects.get_or_create(profile=profile, complete=False )
            items = order.orderitem_set.all()
        else:
            items=[]
            order ={'get_cart_total':0, 'get_cart_item':0}
        context = {'items':items, 'order':order}
    else:
        msg = 'panier vide, <a href="/">ajouter</a> des produits'
        context = {'msg':msg, 'user':user}
    return render(request, 'store/cart.html', context)

# ========================Checkout view=======================


def checkout(request):
    user = request.user
    if user.is_authenticated:
        profile = user.profile
        order, created = Order.objects.get_or_create(profile=profile, complete=False )
        items = order.orderitem_set.all()
    else:
        items=[]
        order ={'get_cart_total':0, 'get_cart_item':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)


# =====================Profile view==========================




def category(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'store/category.html', context)
