from django.contrib import admin
from .models import Post, Comment, Author
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('post_content',)
class AuthorAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('author_icon',)



admin.site.register(Author,AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
# admin.site.register(PostCategory)
# admin.site.register(OneTimeCode)