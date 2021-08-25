from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'text-align: left;'
                                                                    'min-height: 5rem;'}))
    # 글을 쓰는 공간에 class를 editable로 변경 한다.
    #장고의 폼즈를 가져오기
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content'] # 클라이언트에게서 어떤 정보를 받을지

