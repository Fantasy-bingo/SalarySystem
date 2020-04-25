from django.db import models

# Create your models here.
# 薪资组成模型


class SalaryInfo(models.Model):
    # salary_id = models.IntegerField(verbose_name='薪资ID', auto_created=True)
    acct_id = models.CharField(verbose_name='员工账号', max_length=16)
    dept_id = models.IntegerField(verbose_name='部门ID')
    post_id = models.IntegerField(verbose_name='岗位ID')
    year = models.IntegerField(verbose_name='年份')
    month = models.IntegerField(verbose_name='月份')
    attendance = models.IntegerField(verbose_name='出勤天数')
    travel_num = models.IntegerField(verbose_name='出差天数')
    basic_wage = models.IntegerField(verbose_name='基本工资')
    performance = models.IntegerField(verbose_name='绩效奖金')
    allowance = models.IntegerField(verbose_name='津贴')
    insurance = models.FloatField(verbose_name='保险', max_length=16)
    provident_fund = models.IntegerField(verbose_name='公积金')
    travel_fund = models.IntegerField(verbose_name='出差补贴')
    pre_tax_wages = models.FloatField(verbose_name='税前工资', max_length=32)
    actual_salary = models.FloatField(verbose_name='实发工资', max_length=32)

    class Meta:
        verbose_name = '员工薪资信息'
        verbose_name_plural = '员工薪资信息'

    def __str__(self):
        return self.acct_id
