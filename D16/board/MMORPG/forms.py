from django_summernote.widgets import SummernoteWidget
from .models import Post
from django.forms import ModelForm


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
        fields = ['post_header','post_category','post_content',]
        widgets = {
            'post_content': SummernoteWidget(),
        }
