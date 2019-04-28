from ..models import Post,Category
from django import template


num = 5 #定义获取多少个最新的文章

#定义函数为模板标签
register = template.Library()
# 实例化template.Library类，使用装饰器，将函数变为模板标签
# 获取最新的文章，这里获取前5个
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]

#按月份的归档模板标签
@register.simple_tag
def archives():
    # dates 返回一个创建时间的列表，精确到月份
    return Post.objects.dates('create_time','month',order='DESC')

@register.simple_tag()
def get_categories():
    return Category.objects.all()