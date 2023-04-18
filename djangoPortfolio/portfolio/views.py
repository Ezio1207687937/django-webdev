from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment,Blog
from .forms import CommentForm

def blog_list(request):
    blogs = Blog.objects.all() # 这句代码的作用是从Blog模型中获取所有的对象。Blog.objects是一个Manager对象，它提供了许多方法来查询数据库中的数据。all()方法返回一个QuerySet对象，它包含了所有Blog对象的列表。这个QuerySet对象可以被进一步过滤、排序等操作1。
    return render(request, 'portfolio/blog_list.html', {'blogs': blogs})


# 创建文章列表视图
def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'portfolio/post_list.html', {'posts': posts})


# 定义文章详情视图函数
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all().order_by('pub_date')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'portfolio/post_detail.html', {'post': post, 'comments': comments, 'form': form})


