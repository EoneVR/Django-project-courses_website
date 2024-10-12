from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Courses, Comments, Profile, Request


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'description', 'image', 'month', 'price', 'language', 'date_of_start']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'month': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'language': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date_of_start': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            })
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Comment', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 4,
        'cols': 135
    }))

    class Meta:
        model = Comments
        fields = ['content']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
        widgets = {
            'bio': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }


class EditUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class RequestForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-top-0 border-right-0 border-left-0 p-0'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control border-top-0 border-right-0 border-left-0 p-0'
    }))
    topic = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-top-0 border-right-0 border-left-0 p-0'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-top-0 border-right-0 border-left-0 p-0'
    }))

    class Meta:
        model = Request
        fields = ['name', 'email', 'topic', 'description']
