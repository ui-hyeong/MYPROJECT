from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE, # 연결을 시켜준다. 유저객체가 삭제되었을때 어떻게 반응할지 (casecade로 설정했으므로 종속되었다.)
                                  related_name='profile')  # user.profile 이렇게 연결 가능하게 해주는 설정



    image = models.ImageField( upload_to='profile/', null=True )
    nickname = models.CharField(  max_length=30, unique=True, null=True  )
    message = models.CharField( max_length=200, null= True)