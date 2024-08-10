# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import BUSES, DRIVERS, CONDUCTORS, ROUTES, PASSENGERS


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


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

def join1(request):
    if request.method == "POST":
        form = Driverform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('There was an error in your application!'))
            return redirect('driversignup')
        messages.success(request, ('Application submitted successfully!'))
        return redirect('home')

    else:
        return render(request, 'driversignup.html', {})

def join2(request):
    if request.method == "POST":
        form = Conductorform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('There was an error in your application!'))
            return redirect('conductorsignup')
        messages.success(request, ('Application submitted successfully!'))
        return redirect('home')

    else:
        return render(request, 'conductorsignup.html', {})


def tables_view(request):
    all_buses = BUSES.objects.all()
    all_drivers = DRIVERS.objects.all()
    all_conductors = CONDUCTORS.objects.all()
    all_routes = ROUTES.objects.all()
    all_passengers = PASSENGERS.objects.all()

    context = {
    'all_buses': all_buses,
    'all_drivers': all_drivers,
    'all_conductors': all_conductors,
    'all_routes': all_routes,
    'all_passengers': all_passengers,
    }

    return render(request, 'home/tables.html', context)