from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, Lesson, Mark
from datetime import date


class LoginForm(AuthenticationForm):
    pass


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'middle_name', 'password1', 'isStudent']


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
        exclude = ('student', 'date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lesson'].queryset = Lesson.objects.filter(date=date.today())

        # Make the query here
        # lessons = Lesson.objects.filter(date=date.today())
        # self.fields['lesson'] = forms.ChoiceField(choices=((x.pk, x) for x in lessons))





