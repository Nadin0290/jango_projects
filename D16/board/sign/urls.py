from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import loginPage,profilePage,registerPage

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/',LogoutView.as_view(template_name = 'sign/logout.html'), name='logout'),
    # path('signup/', BaseRegisterView.as_view(), name='signup'),
    path('register/',registerPage, name='signup'),
    path('profile/', profilePage, name='profile'),
]