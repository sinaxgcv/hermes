from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200, blank=True, default="")
    last_name = models.CharField(max_length=200, blank=True, default="")

    def __repr__(self):
        return f"Subscriber ID {self.id} <{self.email}>"

    def __str__(self):
        return self.email
