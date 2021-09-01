
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='maram', email='maramankir5@gmail.com',password='maram123321'
        )
        self.snack = Snack.objects.create(
            title='donut',
            purshaser=self.user,
            description='chocolate donut '
        )

    def test_snack_list_view(self):
        actual= self.client.get(reverse('snack_list')).status_code
        self.assertEqual(actual,200)


    # def test_snack_details_view(self):
    #     actual = self.client.get(reverse('snack_detail', args='1')).status_code
    #     self.assertEqual(200, actual)

    # def test_snack_create_view(self):
    #     actual = self.client.post(reverse('create_snack'),{'title': 'donut', ' purshaser': self.user,'description': 'chocolate donut ',})
    #     self.assertEqual(200, actual.status_code)
    #     self.assertContains(actual, 'chocolate donut')
    #     self.assertContains(actual, 'maram')
        
    # def test_snack_update_view(self):
    #     actual = self.client.get(reverse('update_snack', args='1')).status_code
    #     self.assertEqual(200, actual)

    # def test_snack_delete_view(self):
    #     actual = self.client.get(reverse('delete_snack', args='1')).status_code
    #     self.assertEqual(200, actual)
   
    # def test_string_representation(self):
    #     snack_str = Snack(title='donut')
    #     self.assertEqual(str(snack_str),self.snack.title)

