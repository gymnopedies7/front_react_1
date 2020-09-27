from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','photo_tag','message_length','is_public','message','created_at','updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def message_length(self, post):
        return f"{len(post.message)} 글자"

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None
 
        # 기본적으로 장고는 보안문제로, 이미지 링크를 걸어도 바로 안들어감. 따라서 mark_safe를 걸어주면 바로보임