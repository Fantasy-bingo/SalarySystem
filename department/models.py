from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.
# 部门模型，进行表字段定义及说明


class DeptInfo(models.Model):
    # dept_id = models.IntegerField(verbose_name='部门ID', auto_created=True)
    dept_name = models.CharField(verbose_name='部门名称', max_length=50)
    dept_desc = models.CharField(verbose_name='部门描述', max_length=2000)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '部门信息'
        verbose_name_plural = '部门信息'

    def __str__(self):
        return self.dept_name
