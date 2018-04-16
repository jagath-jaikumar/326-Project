from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
