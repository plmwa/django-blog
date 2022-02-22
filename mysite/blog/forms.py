from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm): # DjangoのModelFormでは強力なValidationを使える

    class Meta:
        model = Post # Post モデルと接続し、Post モデルの内容に応じてformを作ってくれる
        fields = ('title', 'text') # 入力するカラムを指定