from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
urlpatterns = [
    path('' , MainView.as_view(), name = 'main_page'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('myposts/',AuthorView.as_view(), name='author_posts'),
    path('myposts/replies/<int:pk>', RepliesView.as_view(), name='post_replies'),
    # path('search/', NewsSearch.as_view()),
    # path('add/', NewCreateView.as_view(), name='new_create'),

    # path('subscribe/',SubscribeView.as_view(), name='subscribe'),

    # path('set_author/',upgrade_me, name='set_author'),
    # path('set_counter', reset_counter, name='set_counter'),

]