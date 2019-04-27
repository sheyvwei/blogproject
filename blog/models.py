from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
    '''分类'''
    name= models.CharField(max_length=200)
    #返回内容  在 Python2中应该使用 __unicode__(self))  或者使用装饰器兼容python2：@python_2_unicode_compatible
    def __str__(self):
        return self.name


class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    '''文章各个字段'''
    #标题
    title = models.CharField(max_length=70)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    ##摘抄
    excerpt = models.CharField(max_length=200, blank=True)
    #分类， 一个文章属于哪一类
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #标签，一个文章有多个标签， 一个标签多篇文章
    tags = models.ManyToManyField(Tag,blank=True)
    #作者 ， 这是从django.contrib.auth.models 导入的类
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #生成url
    #reverse  import django.urls  blog:detail   urls中 app_name='blog' 应用下的 name为detail的连接
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk': self.pk})