from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lists.models import List


def login(request):
    return render(request, "core/login.html", {})


@login_required
def list_overview(request):
    lists = List.objects.all()

    query = request.GET.get("query")
    if query:
        lists = lists.filter(name__icontains=query)

    return render(request, "lists/overview.html", {"lists": lists})
