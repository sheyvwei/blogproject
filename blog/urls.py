from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'index', views.index,name='main'),
    url(r'firstTemplateView', views.firstTemplateViews,name='fff'),
    url(r'postAllView',views.postAllView),
]
