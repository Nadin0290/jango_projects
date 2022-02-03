# from django.shortcuts import render
from typing import Counter
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView,FormView
from django.views.generic.base import View
from .models import Author, Post, Category, Subscriber
from .filters import NewsFilter
from django.core.paginator import Paginator

import datetime


from .forms import PostForm, CategoryForm
#D5
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
#D6
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string
from django.core.mail import mail_admins # импортируем функцию для массовой отправки писем админам
from django.contrib.auth.models import Group
# import logging

# logger = logging.getLogger(__name__)


# Create your views here.
class NewsList(ListView):
    # logger.info('INFO') # что бы я не крутил, в файл general.log ничего не записывается кроме StatReloader:(
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.all()
    ordering = ['-rating']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.date(2021,10,22)   #datetime.utcnow()  # добавим переменную текущей даты time_now
        return context



class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = ['-rating']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'



# дженерик для создания новости
class NewCreateView(PermissionRequiredMixin,CreateView):
    permission_required = ('NewsApp.add_post',)
    template_name = 'news_app/new_create.html'
    form_class = PostForm
    # model = Subscriber
    # queryset = Subscriber.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['is_reported'] = not self.request.user.groups.filter(name = 'authors').exists()
        #context['is_author'] = Author.objects.filter(id = self.request.user.id).exists()
        context['is_author'] =  Author.objects.filter(author_name = self.request.user).exists()
        context['authors'] = Author.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        author = Author.objects.get(author_name = self.request.user)# находим автора (пользователя)
        author.counter() # задаем счетчик +1
        author.save()
        if author.is_blocked: # убираем с групы авторов
            ban_user(request)

        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса


        if form.is_valid():
            form.save()


        return redirect('/news/')

# баним пользователя (убераем с группы автором)
@login_required
def ban_user(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    #authors_group.user_set.remove(user)
    user.groups.remove(authors_group)
    return redirect('/news/')


# становимся автором что бы получить доступ к доп полям (группу исспользуем как для проверки доступа)
@login_required
def upgrade_me(request):
    user = request.user
    if user not in Author.objects.all():
        author = Author(author_name_id = user.id)
        author.save()
    return redirect('/news/add/')


# обнуляем счетчик
@login_required
def reset_counter(request):
    author = Author.objects.get(author_name = request.user)
    author.count_post = 0
    author.is_blocked = False
    authors_group = Group.objects.get(name='authors')
    authors_group.user_set.add(request.user)
    author.save()
    return redirect('/news/')



# дженерик для удаления новости
class NewDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = ('NewsApp.delete_post',)
    model = Post
    context_object_name = 'new'
    template_name = 'news_app/new_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


# дженерик для редактирования новости
class NewUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = ('NewsApp.change_post',)
    template_name = 'news_app/new_create.html'
    form_class = PostForm
    success_url = 'sign/signup/'

    def get_object(self,**kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

# дженерик для для получения деталей о новости
class NewDetailView(DetailView):
    # logger.info('INFO')
    model = Post
    context_object_name = 'new'
    template_name = 'news_app/new_detail.html'
    queryset = Post.objects.all()


# добавляем подписчика в БД
class SubscribeView(ListView):
    model = Subscriber
    template_name = 'news_app/subscribe.html'
    context_object_name = 'subscriber'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subscribers'] = Subscriber.objects.all()
        return context

    def post(self,request,*args, **kwargs):
        user = request.user
        email = request.POST['email']
        category = request.POST['category']
        subscriber = Subscriber(user = user, email = email, category_id = category)
        subscriber.save()

        return super().get(request, *args, **kwargs)  # отправляем пользователя обратно на GET-запрос.
