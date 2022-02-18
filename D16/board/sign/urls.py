from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, BaseProfileView, loginPage

urlpatterns = [
    # path('register/', RegisterView.as_view(),name='my_register'),
    # path('register/code', Register2View.as_view(), name='my_register2'),
    # path('../accounts/login/',
    #      LoginView.as_view(template_name = 'sign/login.html'),
    #      name='login'),
    path('login/', loginPage, name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
    path('../accounts/signup/',
        BaseRegisterView.as_view(template_name = 'sign/signup.html'),
        name='signup'),
        path('profile/', BaseProfileView.as_view()),
    #  path('upgrade/',upgrade_me,name = 'upgrade'),
]