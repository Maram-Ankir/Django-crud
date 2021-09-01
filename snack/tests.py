from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack
class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="maram", email="maramankir5@gmail.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="", description=":A cookie is a baked or cooked snack or dessert that is typically small, flat and sweet. It usually contains flour, sugar, egg, and some type of oil, fat, or butter. It may include other ingredients such as raisins, oats, chocolate chips, nuts, etc", purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Cookies")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "Cookies")
        self.assertEqual(f"{self.snack.purchaser}", "maram")
        self.assertEqual(f"{self.snack.description}", "A cookie is a baked or cooked snack or dessert that is typically small, flat and sweet. It usually contains flour, sugar, egg, and some type of oil, fat, or butter. It may include other ingredients such as raisins, oats, chocolate chips, nuts, etc")


    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "donut")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "purchaser: maram")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                 "title": "donut",
                "description": "chocolate donut",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "Details about donut")



    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated name","description":"3","purchaser":self.user.id}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)