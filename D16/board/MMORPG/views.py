from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from .models import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string
# Create your views here.
from .forms import SignUpForm, CheckForm

class MainView(TemplateView):
    template_name = 'MMORPG/index.html'
class FeedbackView(TemplateView):
    template_name = 'MMORPG/Feedback.html'

# class RegisterAuthView(TemplateView):
#     model = User
#     template_name = 'MMORPG/code_auth.html'

#     def post(self,request, *args,**kwargs):
#         code = request.POST['code']
#         if OneTimeCode.objects.filter(code=code, user__username=self.request.user).exists():
#             login(request, request.user)
#         else:
#             print('auth problem')

#         return super().get(request, *args, **kwargs)  # отправляем пользователя обратно на GET-запрос.

# class RegistrationView(TemplateView):
#     model = User
#     template_name = 'MMORPG/Registration.html'
#     context_object_name = 'user'


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['clicked'] =  User.objects.get(id=self.request.user.id, is_active=True)
#         return context

def signup(request):
    # if request.method == 'POST':
    form = SignUpForm(request.POST)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('../registration/')
    return render(request, 'MMORPG/Registration.html', {'form': form})




def mail(username,email,code):
        html_content = render_to_string(
            'MMORPG/mail.html',
            {
                'username': username,
                'code':code,
            }
        )

        msg = EmailMultiAlternatives(
            subject= f'Подтвердите вашу почту, {username}!',
            from_email= 'arseniy.reima@gmail.com',
            to=[email],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем


# def post(self,request, *args,**kwargs):

#     username = request.POST['username']
#     password = request.POST['password']
#     email = request.POST['email']
#     user = authenticate(request, username=username, password=password,email=email)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         redirect('registration/') # arsemon8@gmail.com
#     else:
#         print('NO!')
#         # Return a 'disabled account' error message
#         ...
#     # if user is not None:
#     #     code = OneTimeCode.objects.create(code=Random.choice('DFKJDHLSGFASDQEWR'))
#     #     code.save()
#     #     mail(username,email,code)
#     #     if OneTimeCode.objects.filter(code=code, user__username=request.user).exists():
#         # redirect('registration/') # arsemon8@gmail.com

#     return super().get(request, *args, **kwargs)  # отправляем пользователя обратно на GET-запрос.