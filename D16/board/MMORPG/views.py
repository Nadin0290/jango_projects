from logging import exception
from pickletools import read_uint1
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView,ListView,DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import authenticate, login
from .models import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import *
from random import randint
from .filters import PostFilter

from django.contrib import messages

# class MainView(ListView):
#     model = Post
#     template_name = 'MMORPG/index.html'
#     context_object_name = 'posts'
#     queryset = Post.objects.all()

#     def post(self,request, *args, **kwargs):
#         post_id = request.POST.get('cur_post_id', None)
#         if post_id is not None:
#             post = Post.objects.get(id=post_id)
#             post.like()
#             post.save()
#         return super().get(request)

def indexPage(request): #ready
    posts = Post.objects.all()

    if request.method == 'POST':
        post_id = request.POST.get('cur_post_id', None)
        if post_id is not None:
            try:
                post = Post.objects.get(id=post_id)
                post.like()
                post.save()
                return redirect('main_page')
            except:
                messages.error(request, 'Something wrong with post')


    context = {'posts':posts, }
    return render(request,'MMORPG/index.html', context)

# class AuthorView(ListView):
#     model = Post
#     template_name = 'MMORPG/author_posts.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         authors_posts = Post.objects.filter(post_author__author_name=user)
#         context['author_posts'] = authors_posts
#         context['filter'] = PostFilter(self.request.GET, queryset=authors_posts)
#         return context

def authorPage(request): #proccess
    user = request.user
    author_posts = Post.objects.filter(post_author__author_name=user)
    filter = PostFilter(request.GET, queryset=author_posts)

    if request.method == 'POST':
        post_id = request.POST.get('cur_post_id', None)
        if post_id is not None:
            try:
                post = Post.objects.get(id=post_id)
                post.like()
                post.save()

            except:
                messages.error(request, 'Something wrong with post')


    context = {'author_posts':author_posts, 'filter': filter}
    return render(request,'MMORPG/author_posts.html', context)


class RepliesView(ListView):
    model = Comment
    template_name = 'MMORPG/post_replies.html'
    context_object_name = 'commentss'
    queryset = Comment.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get('pk',None)
        context['comments'] = Comment.objects.filter(comment_post__id=post_id, comment_online=False)
        # context['comments'] = Comment.objects.all()
        return context

    def post(self,request, pk):
        user = self.request.user
        good_sign = self.request.POST.get('get_id')
        bad_sign = self.request.POST.get('delete_id')
        if good_sign is not None:
            id = good_sign
            comment = Comment.objects.get(id=id)
            comment.comment_online = True
            comment.save()
        if bad_sign is not None:
            id = bad_sign
            comment = Comment.objects.get(id=id)
            comment.delete()
        return super().get(request)


class FeedbackView(TemplateView):
    template_name = 'MMORPG/Feedback.html'

# class LoginAuthView(PermissionRequiredMixin,TemplateView):
#     template_name = 'MMORPG/login.html'
#     success_url= '/registration/'

#     def post(self,request, *args,**kwargs):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('../registration/')
#         return super().get(request, *args, **kwargs)


# после рефактроинга
def postCreatePage(request):
    user = request.user
    form = PostForm(request.POST)
    if request.method == 'POST':
        if user.has_perm('MMORPG.change_post'):
            if form.is_valid():
                post = form.save()
                return redirect(f'{post.get_absolute_url()}')
        else:
            messages.error("You don't have permission!")


    context = {'form':form}
    return render(request,'MMORPG/post_create.html', context)



# после рефактроинга
def postUpdatePage(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    user = request.user
    if request.method == 'POST':
        if user.has_perm('MMORPG.change_post'):
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('main_page')
            else:
                messages.error("Something went wrong!")
        else:
            messages.error("You don't have permission!")


    context = {'form':form}
    return render(request,'MMORPG/post_create.html', context)


# после рефактроинга
def postDetailPage(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(comment_post__id=post.id, comment_online=True)
    user = request.user
    if request.method == 'POST':
        if user.has_perm('MMORPG.view_post'):
            comment = request.POST.get('text')
            Comment.objects.create(comment_text=comment, comment_user=user, comment_post=post)
            return redirect('main_page')
        else:
            messages.error("You don't have permission!")


    context = {'comments':comments, 'post':post}
    return render(request,'MMORPG/post_detail.html', context)




def edit_profile(request):
    pass

def like_post(request):
    pass



# дженерик для редактирования объявлений
# class PostUpdateView(PermissionRequiredMixin,UpdateView):
#     permission_required = ('MMORPG.change_post',)
#     template_name = 'MMORPG/post_create.html'
#     form_class = PostForm

#     def get_object(self,**kwargs):
#         id = self.kwargs.get('pk')
#         return Post.objects.get(pk=id)

# до рефактроинга
# дженерик для для получения деталей о объявлений
# class PostDetailView(PermissionRequiredMixin,DetailView):
#     permission_required = ('MMORPG.view_post',)
#     model = Post
#     context_object_name = 'post'
#     template_name = 'MMORPG/post_detail.html'
#     queryset = Post.objects.all()


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = kwargs.get('object',None)
#         context['comments'] = Comment.objects.filter(comment_post__id=post.id, comment_online=True)
#         return context

#     def post(self,request, pk, *args, **kwargs):
#         user = request.user
#         comment = request.POST['text']
#         post = Post.objects.get(id=pk)
#         Comment.objects.create(comment_text=comment, comment_user=user, comment_post=post)

#         return super().get(request)

# дженерик для создание объявлений
# class PostCreateView(PermissionRequiredMixin,CreateView):
#     permission_required = ('MMORPG.add_post',)
#     template_name = 'MMORPG/post_create.html'
#     form_class = PostForm

#     def post(self, request):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             form.save()

#         return super().get(request)

