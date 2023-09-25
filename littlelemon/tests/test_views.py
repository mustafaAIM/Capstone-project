from django.test import TestCase
from restaurant.models import MenuItem  

class MenuItemViewTest(TestCase):
    def setup(self):
        MenuItem.objects.create(Title="Tomato Pasta", Price=7.99, Inventory=30)
        MenuItem.objects.create(Title="Bruschetta", Price=5.99, Inventory=30)
        MenuItem.objects.create(Title="Tiramisu", Price=4.99, Inventory=30)
        MenuItem.objects.create(Title="Greek Salad", Price=5.99, Inventory=30)
        MenuItem.objects.create(Title="Strawberry Cheesecake", Price=4.99, Inventory=30)

    def test_get_all(self):
        self.setup()
        expected_items = ['Tomato Pasta : 7.99',
                          'Bruschetta : 5.99',
                          'Tiramisu : 4.99',
                          'Greek Salad : 5.99',
                          'Strawberry Cheesecake : 4.99',]
        MenuItItem_items = MenuItem.objects.all()
        received_expected_items = []
        received_unexpected_items = []
        for item in MenuItItem_items:
            if(str(item) in expected_items):
                #print("Expected:", item)
                received_expected_items.append(item)
            else:
                #print("Unexpected:", item)
                received_unexpected_items.append(item)
        self.assertEqual(len(received_expected_items), len(expected_items))
        self.assertEqual(len(received_unexpected_items), 0)