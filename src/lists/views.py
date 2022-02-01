from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from lists.forms import ListForm
from lists.models import List


def login(request):
    return render(request, "core/login.html", {})


@login_required
def list_overview(request):
    lists = List.objects.all()

    query = request.GET.get("query", "")
    if query:
        lists = lists.filter(name__icontains=query)

    return render(request, "lists/overview.html", {"lists": lists, "query": query})


@login_required
def list_add_edit(request, list_id: int = None):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("lists-overview"))
    else:
        form = ListForm()
    return render(request, "lists/form.html", {"form": form})


@login_required
def list_details(request, list_id: int):
    subscriber_list = get_object_or_404(List, pk=list_id)
    return render(request, "lists/details.html", {"subscriber_list": subscriber_list})
