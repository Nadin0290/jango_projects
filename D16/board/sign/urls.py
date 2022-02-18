from django.urls import path
from .views import loginPage,logoutPage,profilePage,registerPage

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/',logoutPage, name='logout'),
    path('register/',registerPage, name='signup'),
    path('profile/', profilePage, name='profile'),
]