from django import forms
from django.forms import SelectDateWidget
from to_do.models import Tag, Task
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


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
        # widgets = {'deadline': SelectDateWidget()}
        # widgets = {'deadline': DateTimePickerInput()}

    # def __init__(self, *args, **kwargs):
    #     super(TaskCreationForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({
    #             'class': 'form-control'
    #         })
