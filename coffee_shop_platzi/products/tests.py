from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductListViewTest(TestCase):
    def test_product_list_view_status_200(self):
        url = reverse('list_product')
        response = self.client.get(url)
        # breakpoint()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 0)

    def test_product_list_view_status_200_with_products(self):
        url = reverse('list_product')
        Product.objects.create(name="Test Product", price=10.99, description="A test product", available=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 1)
