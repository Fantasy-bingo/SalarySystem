#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：Boyce Chen
@Date   ：2020-04-25 23:39
@Desc   ：
=================================================="""
from django.http import HttpResponseRedirect, HttpResponse


# def login_view(request):
#     return HttpResponse('Hello World')


# test function
def index_view(request):
    return HttpResponse('Hello World')
