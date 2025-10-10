from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInlineAdmin]
    list_display = ['user', 'is_active', 'order_date',]
    search_fields = ('user__username',)
