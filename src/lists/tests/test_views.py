from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse

from lists.models import List
from lists.tests.factories import ListFactory


class ListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test", email="test@example.com")
        cls.list1 = ListFactory(name="List 1")
        cls.list2 = ListFactory(name="List 2")
        cls.list3 = ListFactory(name="Test List")

    def setUp(self):
        self.request_factory = RequestFactory()

    def test_list_overview_unauthenticated(self):
        response = self.client.get(reverse("lists-overview"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("login") + "?next=" + reverse("lists-overview")
        )

    def test_list_overview(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("lists-overview"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lists/overview.html")
        self.assertCountEqual(
            response.context["lists"], [self.list1, self.list2, self.list3]
        )

    def test_list_overview_query(self):
        self.client.force_login(self.user)
        url = reverse("lists-overview") + "?query=test"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lists/overview.html")
        self.assertCountEqual(response.context["lists"], [self.list3])

    def test_list_create_unauthenticated(self):
        response = self.client.get(reverse("lists-create"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("login") + "?next=" + reverse("lists-create")
        )

    def test_list_create(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("lists-create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lists/form.html")

        data = {"name": "Test List Creation", "description": ""}
        response = self.client.post(reverse("lists-create"), data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("lists-overview"))
        created_list = List.objects.latest("id")
        self.assertEqual(created_list.name, "Test List Creation")
