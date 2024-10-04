from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuItemsViewTest(APITestCase):
    def setUp(self):
        self.menu_item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu_item2 = Menu.objects.create(title="Burger", price=150, inventory=50)
        self.url = reverse('menu-items')

    def test_getall(self):
        response = self.client.get(self.url)
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)