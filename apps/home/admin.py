# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import (OrderCodes, RequestCustomer)


class OrderCodesAdmin(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()


class RequestCustomerAdmin(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()



admin.site.register(OrderCodes, OrderCodesAdmin)
admin.site.register(RequestCustomer, RequestCustomerAdmin)