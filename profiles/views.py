from store.models import Product
from django.shortcuts import redirect, render

# Create your views here.
def profile(request):
    user = request.user
    if user.is_authenticated:
        products = Product.objects.all()
        first_name = request.user.first_name
        last_name = request.user.last_name
        context = {"products": products, "first_name": first_name, 'last_name':last_name }
        return render(request, 'profiles/profile.html', context)
    else:
        return redirect('store:index')