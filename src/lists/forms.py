from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, ButtonHolder, Field, Layout, Submit
from django import forms
from django.urls import reverse

from lists.models import List


class ListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        self.helper = FormHelper(self)
        if instance:
            url = reverse("lists-overview")
        else:
            url = reverse("lists-overview")
        cancel_button = HTML(
            f'<a class="btn btn-outline-secondary" href="{url}">Cancel</a>'
        )
        self.helper.layout = Layout(
            Field("name", autofocus=True),
            Field("description"),
            ButtonHolder(
                Submit("submit", "Create List", css_class="btn btn-primary"),
                cancel_button,
            ),
        )

    class Meta:
        model = List
        fields = "__all__"
