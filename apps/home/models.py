# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


class OrderCodes(models.Model):
    orders_number = models.CharField(unique = True, max_length=40, verbose_name='کد سفارش',null=True, blank=True )
    tracking_number = models.CharField(max_length=300, verbose_name='کد رهگیری',null=True, blank=True )
    phone_number = models.CharField(max_length=300, verbose_name='شماره تماس',null=True, blank=True )
    customer = models.CharField(max_length=300, verbose_name='مشتری',null=True, blank=True )

    objects = models.Manager()

    class Meta:
        verbose_name = 'کد رهگیری'
        verbose_name_plural = 'کد های رهگیری'

class RequestCustomer(models.Model):
    orders_number = models.CharField(max_length=40, verbose_name='کد سفارش',null=True, blank=True )
    customer = models.CharField(max_length=300, verbose_name='مشتری',null=True, blank=True )
    status = models.CharField(max_length=300, verbose_name='وضعیت',null=True, blank=True )

    objects = models.Manager()

    class Meta:
        verbose_name = 'مشتری درخواست دهنده'
        verbose_name_plural = 'مشتری های درخواست دهنده'