from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer


class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product") # Permite redireccionar a la URL especificada cuando el formulario es válido

    def form_valid(self, form): 
        # Si el formulario es válido, se guarda el producto
        form.save()
        return super().form_valid(form)

class ProductListView(generic.ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"

class ProductListAPI(APIView):
    authentication_classes = [] # Deshabilitar la autenticación para esta vista
    permission_classes = [] # Deshabilitar los permisos para esta vista
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

   
    
