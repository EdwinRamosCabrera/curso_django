import django
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class MyOrderTests(TestCase): #Cuando entre un usuarrio que no este logueado lo redirija al login
    def test_no_logged_in_user_redirect(self):
        url = reverse('my_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/usuarios/login/?next=/pedidos/add_order_product/')

    def test_logged_in_user_redirect(self):
        url = reverse('my_order')
        user = get_user_model().objects.create(username='test')
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)