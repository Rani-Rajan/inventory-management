# items/tests.py
from rest_framework.test import APIClient
from django.test import TestCase
from .models import Item

class ItemAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {
            "name": "Test Item",
            "description": "Test Description",
            "price": 100.0
        }

    def test_create_item(self):
        # Corrected URL path with '/api/items/'
        response = self.client.post('/api/items/', self.item_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_read_item(self):
        item = Item.objects.create(**self.item_data)
        # Corrected URL path with '/api/items/<id>/'
        response = self.client.get(f'/api/items/{item.id}/')
        self.assertEqual(response.status_code, 200)

    def test_update_item(self):
        item = Item.objects.create(**self.item_data)
        update_data = {"name": "Updated Item", "description": "Updated Description", "price": 150.0}
        # Corrected URL path with '/api/items/<id>/'
        response = self.client.put(f'/api/items/{item.id}/update/', update_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_item(self):
        item = Item.objects.create(**self.item_data)
        # Corrected URL path with '/api/items/<id>/delete/'
        response = self.client.delete(f'/api/items/{item.id}/delete/')
        self.assertEqual(response.status_code, 204)
