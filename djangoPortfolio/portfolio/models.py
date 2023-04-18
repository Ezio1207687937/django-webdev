from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 创建一个名为Post的模型类
class Post(models.Model):
    # 定义CharField，最大长度为200，表示文章的标题
    title = models.CharField(max_length=200)
    # 定义TextField，表示文章的正文内容
    content = models.TextField()
    # 定义DateTimeField，设置默认值为当前时间
    pub_date = models.DateTimeField(default=timezone.now)
    # 定义DateTimeField，自动设置为最后一次保存对象的时间
    updated_date = models.DateTimeField(auto_now=True)

    # 定义一个特殊方法，返回对象的字符串表示形式，本例中返回文章的标题
    def __str__(self):
        return self.title

class Comment(models.Model):
    # 定义外键，关联到Post模型，on_delete参数表示当关联的Post对象被删除时，也同时删除该评论对象。related_name='comments'表示为Post模型和Comment模型之间的关系设置了一个反向关系的名称，该名称为comments。这样，在查询Post对象时可以通过comments属性访问它的所有评论。例如，如果要获取一个名为post的Post对象的所有评论，可以使用post.comments.all()。
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # 定义CharField，表示评论的作者，最大长度为100
    author = models.CharField(max_length=100)
    # 定义TextField，表示评论的内容
    content = models.TextField()
    # 定义DateTimeField，表示评论的发布时间，默认为当前时间
    pub_date = models.DateTimeField(default=timezone.now)

	# 定义一个特殊方法，返回对象的字符串表示形式，本例中返回评论作者和评论内容的前50个字符
    def __str__(self):
        return f"{self.author} - {self.content[:50]}"