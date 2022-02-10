from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContentForm(forms.ModelForm):
    '''Форма добавление контента к статьям'''
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
}

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # password = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2',)

class CheckForm(UserCreationForm):
    code = forms.CharField(max_length=30, required=False, help_text='Required. Inform a valid code from email address.')

    class Meta:
        model = Profile
        fields = ('code',)

