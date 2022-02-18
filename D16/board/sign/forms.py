from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import Group
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','avatar']




# class BasicSignupForm(SignupForm):

#     def save(self, request):
#         user = super(BasicSignupForm, self).save(request)
#         authors = Group.objects.get(name='authors')
#         authors.user_set.add(user)
#         author = Author.objects.create(author_name=user)

#         return user
