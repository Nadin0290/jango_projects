from django.urls import path
from .views import NewsList,NewsSearch,NewCreateView,NewDeleteView,NewDetailView,NewUpdateView,SubscribeView, upgrade_me, reset_counter
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('' , (NewsList.as_view()), name = 'main_page'), #cache_page(60 * 1) полное кеширование страницы тут будет уместно потому что проверка авторизации!
    path('<int:pk>/', (NewDetailView.as_view()), name='new_detail'),
    path('search/', NewsSearch.as_view()),
    path('add/', NewCreateView.as_view(), name='new_create'),
    path('<int:pk>/edit/', NewUpdateView.as_view(), name='new_update'),
    path('<int:pk>/delete/', NewDeleteView.as_view(), name='new_delete'),
    path('subscribe/',SubscribeView.as_view(), name='subscribe'),

    path('set_author/',upgrade_me, name='set_author'),
    path('set_counter', reset_counter, name='set_counter'),

]
# <int:news_post_category_id>