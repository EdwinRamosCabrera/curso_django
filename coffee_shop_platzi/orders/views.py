from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Order
from .forms import OrderProductForm

class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()

class CreateOrderProductView(LoginRequiredMixin, CreateView): # Vista para agregar un producto al pedido
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("my_order")

    def form_valid(self, form): # Asignar el usuario al producto del pedido, form es una instancia de OrderProductForm
        order, _ = Order.objects.get_or_create(user=self.request.user, is_active=True) # Obtener o crear un pedido activo para el usuario, el método get_or_create devuelve una tupla (objeto - en este caso la orden, booleano - si fue o no creada la orden)
        form.instance.order = order # Asignar la orden al producto del pedido
        form.instance.quantity = 1 # Asignar la cantidad 1 al producto del pedido
        form.save() # Guardar el producto del pedido
        return super().form_valid(form) # como estamos sobreescribiendo el método form_valid, debemos llamar al método form_valid de la clase padre para que se ejecute el flujo normal de un CreateView