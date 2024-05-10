# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import (OrderCodes, RequestCustomer)
from core.settings import (SMS_API, WC_API)
from django.shortcuts import render
from django.template import loader
from .forms import IMPORT_EXCEL
from django.urls import reverse
from django import template
from tablib import Dataset
from kavenegar import *


#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@csrf_exempt
def import_excel(request):
    if request.method == 'POST':
        order_code = request.POST.get('order_code')
        tracking_number = request.POST.get('tracking_number')
        customer = request.POST.get('customer')
        phone_number = request.POST.get('phone_number')
        if order_code != '':
            if tracking_number != '':
                if customer != '':
                    if phone_number != '':
                        # SMS SEND TO CUSTOMER
                        try:
                            api = KavenegarAPI(SMS_API)
                            params = {
                                'receptor': phone_number,
                                'template': 'kif123Report',
                                'token': tracking_number,
                                'type': 'sms',
                            }   
                            response = api.verify_lookup(params)
                            print(response)
                        except APIException as e: 
                            print(e)
                        except HTTPException as e: 
                            print(e)
                        # DB => Restore detail on database
                        OrderCodes.objects.create(
                            orders_number=order_code,
                            tracking_number=tracking_number,
                            phone_number=phone_number,
                            customer=customer,
                        )
                        return JsonResponse({'status': 'کد رهگیری با موفقیت افزوده شد', 'success': True})
                    else:
                        # phone number empty
                        return JsonResponse({'status': 'شماره تماس را وارد کنید', 'success': False})
                else:
                    # customer empty
                    return JsonResponse({'status': 'نام مشتری را وارد کنید', 'success': False})
            else:
                # tracking_number empty
                return JsonResponse({'status': 'شماره رهگیری مرسوله پستی را وارد کنید', 'success': False})
        else:
            # order_code empty
            return JsonResponse({'status': 'شماره سفارش را وارد کنید', 'success': False})
    else:
        # Bad request
        return JsonResponse({'status': 'درخواست ارسال شده معتبر نمی باشد', 'success': False})
        
@login_required
def load_upload_page(request):
    return render(request, 'home/upload.html')
    '''
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
    '''

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
        # AAAAAAAAAAAAAAAAAAAAAAAAAA
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