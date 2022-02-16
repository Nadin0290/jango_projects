from django_summernote.widgets import SummernoteWidget
from .models import Post, Author
from django.forms import ModelForm, BooleanField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContentForm(ModelForm):
    '''Форма добавление контента к статьям'''
    class Meta:
        model = Post
        fields = ['post_content']
        widgets = {
            'content': SummernoteWidget(),
}

class PostForm(ModelForm):
    '''Форма создание статей для пользователей (которые вошли в систему)'''
    class Meta:
        model = Post
        fields = ['post_author','post_header','post_category','post_content',]
        widgets = {
            'post_content': SummernoteWidget(),
        }

class AuthorForm(ModelForm):
    '''Форма редактирования автора для пользователей (которые вошли в систему)'''
    class Meta:
        model = Author
        fields = ['author_name','author_icon',]
        widgets = {
            'author_icon': SummernoteWidget(),
        }
# class MailForm(forms.ModelForm):
#     username = forms.CharField(max_length=30, required=True)
#     email = forms.EmailField(max_length=128, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = Profile
#         fields = ('username', 'email',)

# class SignUpForm(forms.ModelForm):
#     username = forms.CharField(max_length=30, required=True)
#     password = forms.CharField(max_length=64,required=True)
#     code = forms.CharField(max_length=30, required=True, help_text='Required. Inform a valid code from email address.')

#     class Meta:
#         model = Profile
#         fields = ('username','password','code',)

