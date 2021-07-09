from django.db import models

# Create your models here.

class newModel(models.Model):  # 장고에서 제공해주는 기본 모델 ( models.Model)
    text = models.CharField(max_length=255, null=False)  # 문자열을 입력받는 것을 만든다. max_length는 최대 문자열 길이를 설정
