from django import forms
from django.core.exceptions import ValidationError

from workers.models import Worker


class WorkerCreateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'salary', 'note']

        labels = {
            'name': "worker's name",
            'salary': "salary",
            'note': "note"
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': "name",
                'class': 'form-control'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'step': '1'
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "note",
                'rows': 5
            })
        }



class WorkerSearchForm(forms.Form):
    name = forms.CharField(
        label="Worker's name:",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter the name',
            'class': 'form-control'
        })
    )
    min_salary = forms.DecimalField(
        label="minimum salary:",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'from',
            'class': 'form-control'
        })

    )

    max_salary = forms.DecimalField(
        label="maximum salary:",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'up-to',
            'class': 'form-control'
        })

    )
    def clean_min_salary(self):
        min_salary =  self.cleaned_data.get('min_salary')
        max_salary = self.cleaned_data.get('max_salary')
        if min_salary or max_salary < 0:
            raise ValidationError("min and max salary can't be lower than zero")

    def clean(self):
        cleaned_data = super().clean()

        min_salary = cleaned_data.get('min_salary')
        max_salary = cleaned_data.get('max_salary')

        if min_salary and max_salary:
            if min_salary >max_salary:
                raise ValidationError("Maximum salary can't be more than minimum salary")
        return cleaned_data
