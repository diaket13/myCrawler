from django.db import models


# Create your models here.
class UserInfo(models.Model):
    # 测试测试
    user = models.CharField(max_length=50, unique=True)
    bpub_date = models.DateField()
    pwd = models.CharField(max_length=50)
    # 逻辑删除，默认不删除
    idDelete = models.BooleanField(default=False)
