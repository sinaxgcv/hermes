from django.urls import path

from lists import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("lists", views.list_overview, name="lists-overview"),
    path("lists/create", views.list_add_edit, name="lists-create"),
    path("lists/<int:list_id>", views.list_details, name="lists-details"),
]
