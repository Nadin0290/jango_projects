from django.forms import ModelForm, BooleanField
from .models import Post, Category



class PostForm(ModelForm):
    check_box = BooleanField(label='Вы автор?')

    class Meta:
        model = Post
        fields = ['author','category_type','header','text','post_category','check_box']

class CategoryForm(ModelForm):
    check_box = BooleanField(label='Вы автор?')

    class Meta:
        model = Category
        fields = ['category_name']


# class SubscribeForm(forms.Form):
#     category = ModelChoiceField(queryset=Category.objects.all())

# class SubscribeForm(ModelForm):

#     class Meta:
#         model = Post
#         fields = ['post_category']





