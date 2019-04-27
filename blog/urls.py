from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'index', views.index,name='main'),
    url(r'firstTemplateView', views.firstTemplateViews,name='fff'),
    url(r'postAllView',views.postAllView),

    #博客的详细页面
    url(r'^post/(?P<pk>[0-9]+)',views.detail,name='detail')
]
