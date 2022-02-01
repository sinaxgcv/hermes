from django.contrib import admin

from lists.models import List, Subscriber


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")
    search_fields = ("email",)
