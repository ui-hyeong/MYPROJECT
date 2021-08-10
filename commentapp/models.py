from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)
    # 위는 작성자와 연결이다.
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)

    #textField는 장문의 글을 받을떄 씀
    content = models.TextField(null=False)

    #datetimefield는 시간과 날짜를 찍어줌
    created_at = models.DateTimeField(auto_now_add=True)