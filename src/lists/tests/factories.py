from factory import Faker
from factory.django import DjangoModelFactory

from lists.models import List, Subscriber


class ListFactory(DjangoModelFactory):
    class Meta:
        model = List


class SubscriberFactory(DjangoModelFactory):
    email = Faker("email")

    class Meta:
        model = Subscriber
