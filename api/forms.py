from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Task


class DateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('deadline',)
        widgets = {
            'deadline': AdminDateWidget(),
        }
