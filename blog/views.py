from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from comments.forms import CommentForm
import markdown
#add vue
from django.http import JsonResponse
from django.core import serializers
import json
import datetime
# Create your views here.


###region使用前后端分离
#保存文章
def add_post(request):
    response = {}
    try:
        create_time = datetime.datetime.now()
        excerpt = request.GET.get('post_excerpt')
        category = request.GET.get('post_category')
        tags = request.GET.get('tags')
        author = request.GET.get('author')
        post = Post(title=request.GET.get('post_title'),body=request.GET.get('post_body'),create_time=create_time)
        post.save()
    except Exception as e:
        response['isEff'] = 0
        response['msg'] = str(e)
    return JsonResponse(response)
#显示文章
def show_post(request):
    response = {}
    try:
        post = Post.objects.filter()
        # json.loads() 解码son数据
        # serializers.serialize()序列化数据
        response['list'] = json.loads(serializers.serialize("json",post,ensure_ascii=False),encoding='utf-8')
        response['msg'] = 'success'
        response['isEff'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['isEff'] = 0
    return JsonResponse(response)

###endregion


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
    #return render(request,'blog/detail.html',context={'post':post})

    ###增加评论数据
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request,'blog/detail.html', context=context)
'''归档页面'''



def archives(request, year, month):
    # post_list = Post.objects.all()
    post_list = Post.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    return render(request, 'blog/postAllView.html',context={'post_list':post_list})

def catogory(request,pk):
    post_list = Post.objects.filter(category=pk).order_by('-create_time')
    return render(request,'blog/postAllView.html',context={'post_list':post_list})

