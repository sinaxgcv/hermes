from factory.django import DjangoModelFactory

from lists.models import List, Subscriber


class ListFactory(DjangoModelFactory):
    class Meta:
        model = List


class SubscriberFactory(DjangoModelFactory):
    class Meta:
        model = Subscriber
