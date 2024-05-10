# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('upload_code', views.load_upload_page, name='upload_code'),
    path('upload', views.import_excel, name='upload'),
    path('', views.index, name='home'),
    path('req', views.req, name='req'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
