from django.db import models
from django.contrib.auth.hashers import make_password

import secrets


# Create your models here.
# 员工模型，进行表字段定义及说明

class EmpInfo(models.Model):
    """
    员工信息类
    """
    MALE = 'M'
    FEMALE = 'F'
    SEX_TYPE = (
        (MALE, '男'),
        (FEMALE, '女')
    )

    OPERATOR = '999'
    EMPLOYEE = '000'
    ROLE_TYPE = (
        (OPERATOR, '管理员'),
        (EMPLOYEE, '员工'),
    )

    # emp_id = models.IntegerField(verbose_name='员工ID', null=False, auto_created=True)
    acct_id = models.CharField(verbose_name='员工账号', max_length=16, db_index=True)
    password = models.CharField(verbose_name='密码', null=False, max_length=2048)
    real_name = models.CharField(verbose_name='员工真实姓名', max_length=64)
    emp_phone = models.IntegerField(verbose_name='联系方式')
    emp_age = models.IntegerField(verbose_name='年龄')
    emp_sex = models.IntegerField(verbose_name='性别', choices=SEX_TYPE)
    address = models.CharField(verbose_name='联系地址', max_length=500)
    emp_role = models.IntegerField(verbose_name='登录角色', null=False, choices=ROLE_TYPE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '员工信息'
        verbose_name_plural = '员工信息'

    def __str__(self):
        return self.real_name

    def save(self, *args, **kwargs):  # 用户登录密码加密,当前盐值为None，后续修改成安全随机数--2020/04/25
        self.password = make_password(self.password, salt=None, hasher='pbkdf2_sha256')
        super(EmpInfo, self).save(*args, **kwargs)
