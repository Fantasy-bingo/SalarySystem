from django.db import models

# Create your models here.
# 出差模型


class TravelInfo(models.Model):
    # travel_id = models.IntegerField(verbose_name='出差信息ID', auto_created=True)
    acct_id = models.CharField(verbose_name='员工账号', max_length=16)
    year = models.IntegerField(verbose_name='年份')
    month = models.IntegerField(verbose_name='月份')
    travel_num = models.IntegerField(verbose_name='出差天数')
    travel_fund = models.IntegerField(verbose_name='出差补贴')
    travel_desc = models.CharField(verbose_name='出差事项说明', max_length=256)

    class Meta:
        verbose_name = '员工出差信息'
        verbose_name_plural = '员工出差信息'

    def __str__(self):
        return self.travel_id

