# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import (OrderCodes, RequestCustomer)
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import loader
from .forms import IMPORT_EXCEL
from django.urls import reverse
from django import template
from tablib import Dataset


#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required
def import_excel(request):
    context = {'status':''}
    if request.method == 'POST':
        excel_resource = IMPORT_EXCEL()
        dataset = Dataset()
        new_excel = request.FILES['myfile']
        imported_data = dataset.load(new_excel.read(), format='xlsx')
        for data in imported_data :
            value = OrderCodes(
                data[0],
                data[1],
                data[2],
                data[3],
            )
            value.save()
        context['status'] = 'درون ریزی محصول با موفقیت انجام شد'
    else:
        context['status'] = 'درون ریزی فایل کد های رهگیری' 
    return render(request, 'home/upload.html', context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@csrf_exempt
def req(request):
    order_code = request.POST.get('order_code')
    order = OrderCodes.objects.filter(orders_number = order_code)
    if order:
        # Create a loop for retrive data from database
        for data in order:
            customer = data.customer
            tracking_number = data.tracking_number
        # Create request objects
        RequestCustomer.objects.create(
            orders_number = order_code,
            customer = customer,
            status = 'موفق',
        )
        # return response
        return JsonResponse({
            'status': 'موفقیت آمیز',
            'customer': customer,
            'tracking_number': tracking_number,
            'success': True,
        })
    else:
        # Create request objects
        RequestCustomer.objects.create(
            orders_number = order_code,
            customer = 'درخواست دهنده',
            status = 'ناموفق',
        )
        # return response
        return JsonResponse({
            'status': 'ناموفق',
            'success': False,
        })