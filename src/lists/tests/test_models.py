from django.test import TestCase

from lists.models import Subscriber


class SubscriberTest(TestCase):

    def test_repr(self):
        subscriber = Subscriber.objects.create(email="jack@example.com")

        expected_repr = f"Subscriber ID {subscriber.id} <{subscriber.email}>"
        self.assertEqual(
            expected_repr,
            subscriber.__repr__()
        )

    def test_str(self):
        subscriber = Subscriber.objects.create(email="jack@example.com")

        expected_str = subscriber.email
        self.assertEqual(
            expected_str,
            subscriber.__str__()
        )
