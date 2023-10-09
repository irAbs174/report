# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import (OrderCodes, RequestCustomer)


class OrderCodesAdmin(admin.ModelAdmin):
    list_display = ('orders_number', 'tracking_number', 'customer', )
    search_fields = ('orders_number', 'tracking_number', 'customer', )


class RequestCustomerAdmin(admin.ModelAdmin):
    list_display = ('orders_number', 'customer', 'status', )
    list_filter = ('status',)
    search_fields = ('orders_number', 'customer', 'status', )



admin.site.register(OrderCodes, OrderCodesAdmin)
admin.site.register(RequestCustomer, RequestCustomerAdmin)