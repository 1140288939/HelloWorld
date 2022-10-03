# Create your models here.
from django.db import models

#类名代表了数据库表名
# 表名组成结构为：应用名_类名（如：TestModel_test）。
class test1(models.Model):
    name = models.CharField(max_length=20)
    hobby = models.CharField(max_length=20)