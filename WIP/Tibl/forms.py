from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']


class AddSearchedClassForm(forms.Form):
    def __init__(self, choices, *args, **kwargs):
        super(AddSearchedClassForm, self).__init__(*args, **kwargs)
        self.fields['sections'] = forms.MultipleChoiceField(
        	widget=forms.CheckboxSelectMultiple,
            choices=choices,
        )
