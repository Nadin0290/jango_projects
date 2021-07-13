from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['len'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
    #     return context 

class DetailList(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
