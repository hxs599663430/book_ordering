from django.db import models

from datetime import datetime
# Create your models here.
from django.db.models import Manager


class Logs(models.Model):
    objects = Manager()
    id = models.IntegerField(verbose_name="序号", auto_created=True)
    log_id = models.CharField(verbose_name="日志编号", primary_key=True, max_length=20)
    name = models.CharField(verbose_name="客户/员工名称", max_length=100, null=True, blank=True)
    somethings = models.CharField(verbose_name="执行事件", max_length=100, null=True, blank=True)
    runtime = models.DateTimeField(verbose_name="执行时间", default=datetime.now)

    class Meta:
        verbose_name = "日志信息表"

    def __str__(self):
        return self.log_id
