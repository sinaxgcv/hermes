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

    def test_subscriber_count(self):
        list_1 = ListFactory(name="List1")
        list_2 = ListFactory(name="List2")

        subscriber1 = SubscriberFactory()
        subscriber1.lists.add(list_1)

        subscriber2 = SubscriberFactory()
        subscriber2.lists.add(list_1)

        subscriber3 = SubscriberFactory()
        subscriber3.lists.add(list_2)

        self.assertEqual(list_1.subscriber_count, 2)

        self.assertEqual(list_2.subscriber_count, 1)


class SubscriberTest(TestCase):
    def test_repr(self):
        subscriber = SubscriberFactory(email="jack@example.com")

        expected_repr = f"Subscriber ID {subscriber.id} <{subscriber.email}>"
        self.assertEqual(expected_repr, subscriber.__repr__())

    def test_str(self):
        subscriber = SubscriberFactory(email="jack@example.com")

        expected_str = subscriber.email
        self.assertEqual(expected_str, subscriber.__str__())
