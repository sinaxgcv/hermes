from django.urls import path

from lists import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("lists", views.list_overview, name="lists-overview"),
]
