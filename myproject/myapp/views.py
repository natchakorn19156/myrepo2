# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse
import datetime
import pytz
from .models import Product

def current_datetime(request):

    # now = datetime.datetime.now()
    # myhome = pytz.timezone('Asia/Bangkok')
    # utctime = datetime.datetime.utcnow()
    time = datetime.datetime.today()
    local = time.timetuple()
    # now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc())
    html = "<html><body>It is now %s.</body></html>" % time
    return HttpResponse(html)

def list_products(request):
    text ="" 
    head = "<br \>" + "<center>" + "<h1>" + "List Product" + "</h1>"+"</center>"
    for i in Product.objects.all():
        text = "<center>" + text+ "<li \>" + str(i) + "<br \>" + "</center>"
    
    return HttpResponse(head+text)

# Create your views here.

def products_detail(request):
    text = ""
    head = "<br \>" + "<center>" + "<h1>" + "Product" + "</h1>"+"</center>"
    for i in Product.objects.all():
        name = "<center \>"+ "Name : " + str(i) + "<br \>"
        price2 = "Price : " + str(i.price) + " Bath" + "<br \>"
        cate = "Category : " + str(i.category) + "<br \>" + "________________________________" + "<br \>"
        text = text+name + price2 + cate

    return HttpResponse(head+text)