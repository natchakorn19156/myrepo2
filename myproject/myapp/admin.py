# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    fields = ('name','price','category')

admin.site.register(Product,ProductAdmin)

# Register your models here.
