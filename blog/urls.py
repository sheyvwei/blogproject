from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$',views.postAllView),
    url(r'index', views.index,name='index'),
    url(r'firstTemplateView', views.firstTemplateViews,name='fff'),
    url(r'postAllView',views.postAllView, name='main'),
    #博客的详细页面
    url(r'^post/(?P<pk>[0-9]+)',views.detail,name='detail'),
    #归档路径
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    #分类搜索
    url(r'^category/(?P<pk>[0-9]+)/$',views.catogory,name='category'),
    #url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    ### add  vue
    url(r'show_post', views.show_post),
    url(r'add_post', views.add_post)
]
