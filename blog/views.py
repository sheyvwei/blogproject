from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def index(request):
    return HttpResponse("HttpReponse返回首页")


def firstTemplateViews(request):
    return render(request,'blog/index.html', context={'title':'我的博客首页',
                                                            'welcome': '使用模板页'})

'''使用render返回模板视图'''

def postAllView(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request,'blog/postAllView.html',context={'post_list':post_list})