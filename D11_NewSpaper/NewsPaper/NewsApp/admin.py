from django.contrib import admin
from .models import Author, Category, Post, Comment, PostCategory,Subscriber

# Register your models here.

# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'category_type', 'rating', 'author') # оставляем только имя и цену товара
    list_filter = ('header','rating') # добавляем примитивные фильтры в нашу админку
    search_fields = ('header','text') # тут всё очень похоже на фильтры из запросов в базу

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_rating')

# class CategoryAdmin(admin.ModelAdmin): # имеет только 1 поле

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'user') # оставляем только имя и цену товара
    list_filter = ('user','comment_text') # добавляем примитивные фильтры в нашу админку
    search_fields = ('comment_text','user__username') # __ так можно обращаться к дочерним полям (точно не знаю как правильно сказать)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email','user','category') # оставляем только имя и цену товара
    list_filter = ('email', 'category') # добавляем примитивные фильтры в нашу админку
    search_fields = ('email','user__username') # тут всё очень похоже на фильтры из запросов в базу

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post_through','category_through') # оставляем только имя и цену товара
    list_filter = ('post_through','category_through') # добавляем примитивные фильтры в нашу админку

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category) # имеет 1 поле поэтому можем только через __str__
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
