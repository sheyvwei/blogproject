from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown
# Create your views here.


def index(request):
    return HttpResponse("HttpReponse返回首页")


def firstTemplateViews(request):
    return render(request,'blog/index.html', context={'title':'我的博客首页',
                                                            'welcome': '使用模板页'})

'''使用render返回模板视图'''
def postAllView(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/postAllView.html', context={'post_list':post_list})

'''博客详细页面'''


def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    #使用markdown
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',  #某些扩展
                                      'markdown.extensions.codehilite',  #代码高亮
                                      'markdown.extensions.toc',  # 。tables表格处理， .toc在文档中生成目录
                                  ])
    return render(request,'blog/detail.html',context={'post':post})

'''归档页面'''



def archives(request, year, month):
    # post_list = Post.objects.all()
    post_list = Post.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    return render(request, 'blog/postAllView.html',context={'post_list':post_list})

def catogory(request,pk):
    post_list = Post.objects.filter(category=pk).order_by('-create_time')
    return render(request,'blog/postAllView.html',context={'post_list':post_list})