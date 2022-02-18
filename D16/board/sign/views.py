from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import BasicSignupForm



class BaseRegisterView(LoginRequiredMixin,TemplateView):
    template_name = 'sign/signup.html'
    form_class = BasicSignupForm

class BaseProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'sign/profile.html'

# после рефактроинга
def loginPage(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main_page')

    context = {}
    return render(request,'sign/login.html', context)


# class RegisterView(TemplateView):
#     template_name = 'sign/register_part1.html'
#     # form_class = AuthorForm
#     # success_url = 'sign/register/code'

#     def post(self, request, *args, **kwargs):
#         email = self.request.POST.get('email')
#         print(email)
#         if not Author.objects.filter(author_email=email).exists():
#             user = MyUser(email=email,code=randint(100,999))
#             user.save()
#             send_code_by_mail(email,user.code)
#             return redirect('/sign/register/code')

#         return super().get(request)

# class Register2View(TemplateView):
#     template_name = 'sign/register_part2.html'
#     success_url = 'sign/signup'

#     def post(self, request, *args, **kwargs):
#         username = self.request.POST.get('username')
#         email = self.request.POST.get('email')
#         code = self.request.POST.get('code')
#         password = self.request.POST.get('password')
#         print(email)
#         print(username)
#         print(code)
#         print(password)
#         if MyUser.objects.filter(email=email,code=code).exists():
#             user = MyUser.objects.get(email=email,code=code)
#             user.username = username
#             user.password = password
#             user.save()
#             login(request, user)

#         return super().get(request, *args, **kwargs)



# @login_required
# def subscribe(self,request):
#     user = request.user
#     categories = Category.objects.get(name= Post.)
#     if user not in categories.subscribers_get(user=user):
#         categories.subsribers_set.add(user)
#     return redirect('/subscribe/')