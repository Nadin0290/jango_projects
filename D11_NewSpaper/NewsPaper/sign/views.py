from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from NewsApp.models import Category

from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required



class BaseRegisterView(LoginRequiredMixin,TemplateView):
    template_name = 'sign/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/sign/signup')




# @login_required
# def subscribe(self,request):
#     user = request.user
#     categories = Category.objects.get(name= Post.)
#     if user not in categories.subscribers_get(user=user):
#         categories.subsribers_set.add(user)
#     return redirect('/subscribe/')