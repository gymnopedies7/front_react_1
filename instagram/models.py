from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    message = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name = '공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message

    def message_length(self, post):
        return len(post.message)
    # message_length.short_description = "메시지 글자수"
    
    class Meta:
        ordering = ['-id']

'''
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_url = models.URLField(blank=True)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(allow_unicode=True, db_index=True)  # allow_unicode : 한글허용
    desc = models.TextField(blank=True)
    image = models.ImageField(blank=True)  # Pillow 설치필요
    comment_count = models.PositiveIntegerField(default=0)
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# on_delete = models.CASCADE : ForeignKeyField를 포함하는 모델 Instance(row)도 함께 삭제한다

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
'''