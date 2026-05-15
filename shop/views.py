from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@login_required
def product_page(request):
    return render(request, 'products.html')