from django.urls import path
from .views import NewsList,NewsDetail,NewsSearch,NewCreateView,NewDeleteView,NewDetailView,NewUpdateView

urlpatterns = [
    path('' , NewsList.as_view()),
    path('<int:pk>/',NewDetailView.as_view(), name='new_detail'),
    path('search/', NewsSearch.as_view()),
    path('add/', NewCreateView.as_view(), name='new_create'),
    path('<int:pk>/edit/', NewUpdateView.as_view(), name='new_update'),
    path('<int:pk>/delete/', NewDeleteView.as_view(), name='new_delete'),

]