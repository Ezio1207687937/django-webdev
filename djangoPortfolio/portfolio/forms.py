from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:    # 定义了一个内部类，用于指定表单类基于哪个模型类生成表单字段。
        model = Comment
        fields = ['author', 'content']
        labels = {
            'author': 'Your Name',
            'content': 'Your Comment',
        }
