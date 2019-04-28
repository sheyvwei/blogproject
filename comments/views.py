from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm
# Create your views here.


def post_comment(request,post_pk):
    #获取被评论的wenzhang
    post = get_object_or_404(Post,pk=post_pk)
    if request.method == 'POST':
        #用户提交的数据在request.POST中
        #用这些数据构造CommentForm实例，表单就生成了
        form = CommentForm(request.POST)

        if form.is_valid():
            #判断表单是否正确，如果正确，调用表单的sava方法保存在数据库中

            #commit=False的作用是将表单的数据生成comment实例，但不保存咋数据库中
            comment = form.save(commit=False)

            #将comment的post与此时的post关联起来
            comment.post = post

            comment.save()
            #好重定向
            return redirect(post)
        else:
            #不正确， 重新加载
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request,'blog/detail.html',context)

    return redirect(post)