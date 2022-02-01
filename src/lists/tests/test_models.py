from django.test import TestCase

from lists.tests.factories import ListFactory, SubscriberFactory


class ListTest(TestCase):
    def test_repr(self):
        my_list = ListFactory(name="My List")

        expected_repr = f"List ID {my_list.id} <{my_list.name}>"
        self.assertEqual(expected_repr, my_list.__repr__())

    def test_str(self):
        my_list = ListFactory(name="My List")

        expected_str = my_list.name
        self.assertEqual(expected_str, my_list.__str__())


class SubscriberTest(TestCase):
    def test_repr(self):
        subscriber = SubscriberFactory(email="jack@example.com")

        expected_repr = f"Subscriber ID {subscriber.id} <{subscriber.email}>"
        self.assertEqual(expected_repr, subscriber.__repr__())

    def test_str(self):
        subscriber = SubscriberFactory(email="jack@example.com")

        expected_str = subscriber.email
        self.assertEqual(expected_str, subscriber.__str__())
