from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
urlpatterns = [
    path('' , indexPage, name = 'main_page'),
    path('add/', postCreatePage, name='post_create'),
    path('<int:pk>/',postDetailPage, name='post_detail'),
    path('<int:pk>/like',postLikePage, name='post_like'),
    path('<int:pk>/edit/', postUpdatePage, name='post_update'),
    path('myposts/',authorPage, name='author_posts'),
    path('myposts/replies/<int:pk>', repliesPage, name='post_replies'),
    # path('search/', NewsSearch.as_view()),
    # path('add/', NewCreateView.as_view(), name='new_create'),

    # path('subscribe/',SubscribeView.as_view(), name='subscribe'),

    # path('set_author/',upgrade_me, name='set_author'),
    # path('set_counter', reset_counter, name='set_counter'),

]