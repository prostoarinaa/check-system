from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, Lesson, Mark
from datetime import date


class LoginForm(AuthenticationForm):
    pass


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'fullname', 'password1']


class AddLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['date', 'name', 'lesson_order']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'datetimepicker1'}),
        }


class AddMarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['lesson']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the query here
        # lessons = Lesson.objects.filter(date=date.today())
        # self.fields['lesson'] = forms.ChoiceField(choices=((x.pk, x) for x in lessons))





