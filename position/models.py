from django.db import models

# Create your models here.
# 岗位信息模型


class PositionInfo(models.Model):
    # post_id = models.IntegerField(verbose_name='岗位ID', auto_created=True)
    post_name = models.CharField(verbose_name='职位名称', max_length=32)
    post_level = models.IntegerField(verbose_name='岗位级别')
    salary_standard = models.IntegerField(verbose_name='薪资标准')

    class Meta:
        verbose_name = '岗位信息'
        verbose_name_plural = '岗位信息'

    def __str__(self):
        return self.post_level


