from django.db import models
import datetime
# Create your models here.
# 文章类型
class Tpyes(models.Model):
#     名称
    typename=models.CharField(max_length=200)
#文章
class article(models.Model):
    # 标题
    title = models.CharField(max_length=200)
    # 时间
    create_date = models.DateTimeField(default=datetime.datetime.now)
    # 内容
    content = models.TextField(max_length=200)
    #     类型
    type=models.ForeignKey(Tpyes,on_delete=models.PROTECT)
    #     作者

