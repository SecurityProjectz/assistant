# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def landing(request):
    return TemplateResponse(request, 'home.html')

def guage(request):
    return TemplateResponse(request, 'guage.html')

