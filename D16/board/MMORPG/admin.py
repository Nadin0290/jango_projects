from django.contrib import admin
from .models import Post, Category, Comment, PostCategory
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)



admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostCategory)