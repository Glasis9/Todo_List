from django import forms
from to_do.models import Tag, Task


class TaskCreationForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        initial=0,
    )
    deadline = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(
            attrs={"type": "datetime-local"}
        ),
        required=False
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
