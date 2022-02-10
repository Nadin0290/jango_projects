from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
urlpatterns = [
    path('logout/',
         LogoutView.as_view(template_name = 'MMORPG/logout.html'),
         name='logout'),
    path('' , MainView.as_view(), name = 'main_page'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('registration/', signup, name='registration'),
    # path('registration/check', RegisterAuthView.as_view(), name='register_check'),
    # path('<int:pk>/',NewDetailView.as_view(), name='new_detail'),
    # path('search/', NewsSearch.as_view()),
    # path('add/', NewCreateView.as_view(), name='new_create'),
    # path('<int:pk>/edit/', NewUpdateView.as_view(), name='new_update'),
    # path('<int:pk>/delete/', NewDeleteView.as_view(), name='new_delete'),
    # path('subscribe/',SubscribeView.as_view(), name='subscribe'),

    # path('set_author/',upgrade_me, name='set_author'),
    # path('set_counter', reset_counter, name='set_counter'),

]