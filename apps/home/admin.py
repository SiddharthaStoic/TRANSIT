# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.

from .models import BUSES, DRIVERS, CONDUCTORS, ROUTES, PASSENGERS

# Register your models here.
admin.site.register(BUSES)
admin.site.register(DRIVERS)
admin.site.register(CONDUCTORS)
admin.site.register(ROUTES)
admin.site.register(PASSENGERS)