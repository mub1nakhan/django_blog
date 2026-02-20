from django.shortcuts import render

# Create your views here.
from .models import Product,Category

def products_list(request):
    if request.method == "POST":
        
        name = request.POST.get("name")
        price = request.POST.get("price")
        status_choices = request.POST.get("status_choices")
        category_id = request.POST.get("category")
    
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})