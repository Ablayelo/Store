from django.db.models.query import NamedValuesListIterable
from django.urls import path, re_path
from django.utils.regex_helper import ESCAPE_MAPPINGS
from store import views

app_name='store'
urlpatterns = [
    path('',views.index, name='index'),
    path('product-detail/<int:id>/', views.productDetail, name='product-detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    #('login/',views.loginView, name='login'),
    path('category/', views.category, name='category'),
    path('register/', views.registerUser, name='register'),
    #path('add-to-cart/<int:id>/', views.addToCart, name='add_to_cart')
    path('logout/', views.logout, name='logout')
]
 