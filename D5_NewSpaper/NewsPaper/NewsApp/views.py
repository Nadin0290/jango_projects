# from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post, Category
from .filters import NewsFilter
from django.core.paginator import Paginator

import datetime


from .forms import PostForm, CategoryForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.
class NewsList(ListView):
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():
            form.save()

        return super().get(request,*args,**kwargs)



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
    model = Post
    context_object_name = 'new'
    template_name = 'news_app/new_detail.html'
    queryset = Post.objects.all()


