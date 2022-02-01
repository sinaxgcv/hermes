import uuid

from django.db import models


class List(models.Model):
    name = models.CharField(unique=True, max_length=200)
    description = models.TextField(blank=True, default="")

    def __repr__(self):
        return f"List ID {self.id} <{self.name}>"

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200, blank=True, default="")
    last_name = models.CharField(max_length=200, blank=True, default="")

    confirmation_key = models.UUIDField(default=uuid.uuid4)
    confirmed_on = models.DateTimeField(blank=True, null=True)

    lists = models.ManyToManyField(List)

    def __repr__(self):
        return f"Subscriber ID {self.id} <{self.email}>"

    def __str__(self):
        return self.email
