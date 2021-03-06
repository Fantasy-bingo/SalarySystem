# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-04-25 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acct_id', models.CharField(db_index=True, max_length=16, verbose_name='员工账号')),
                ('password', models.CharField(max_length=2048, verbose_name='密码')),
                ('real_name', models.CharField(max_length=64, verbose_name='员工真实姓名')),
                ('emp_phone', models.IntegerField(verbose_name='联系方式')),
                ('emp_age', models.IntegerField(verbose_name='年龄')),
                ('emp_sex', models.IntegerField(choices=[('M', '男'), ('F', '女')], verbose_name='性别')),
                ('address', models.CharField(max_length=500, verbose_name='联系地址')),
                ('emp_role', models.IntegerField(choices=[('999', '管理员'), ('000', '员工')], verbose_name='登录角色')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '员工信息',
                'verbose_name_plural': '员工信息',
            },
        ),
    ]
