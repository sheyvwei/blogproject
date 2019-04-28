
from django import forms
from .models import Comment

#表单类必须要继承forms.ModelForm或者 forms.Form
class CommentForm(forms.ModelForm):
    #内部Meta类指定表单相关的内容
    class Meta:
        model = Comment  #此表单指定模型为Comment的类
        fields = ['name','email','url','text']  #指定显示的字段

