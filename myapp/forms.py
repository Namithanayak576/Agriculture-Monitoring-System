from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'sex', 'student_class','section', 'phone_number', 'address']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# myapp/forms.py

class SectionForm(forms.Form):
    section = forms.ChoiceField(widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        self.fields['section'].choices = [(section, section) for section in Student.objects.values_list('section', flat=True).distinct()]

from django import forms
from .models import Grade

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'score', 'grade_date']
        widgets = {
            'grade_date': forms.DateInput(attrs={'type': 'date'}),
        }

# forms.py
from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']  # Include the fields you want in the form

from django import forms

class TeacherLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date']
