# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import inspect
from django.db import connection
# Create your views here.

def index(request):
    return render(request,'tutorial/index.html')

def about(request):
    return render(request,'tutorial/about.html')

def learn(request):
    return render(request,'tutorial/learn.html')

def contribute(request):
    return render(request,'tutorial/contribute.html')
def run_vm(request):
    return render(request, 'tutorial/run_vm.html')
def tool_install(request):
    return render(request, 'tutorial/tools_installation.html')
