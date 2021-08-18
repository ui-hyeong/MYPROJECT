from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null =True)

    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True)

    # 유저를 가져오고 삭제시 유저의 게시글이 삭제되지 않고 null유저의 게시글로남고 target_user.article로 접근하게 해준다.
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/')
    # 별도의 article폴더가 생성되면서 이미지가 그 폴더에 저장된다.
    content = models.TextField(null=True) #장문은 textfield를 쓴다.

    created_at = models.DateField(auto_now_add=True, null=True)
    # 언제 작성을 했는지, db가 찍히는 순간? 시간을 찍어준다.