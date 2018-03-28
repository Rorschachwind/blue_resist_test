# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import inspect
from django.db import connection


query_dict = {'1':'SELECT site_id, cfu, ctx FROM plate JOIN agar ON plate.agar_id = agar.agar_id', '2':'two'}

def index(request): # GET
	# create blank forms
	template_name = 'tutorial/index.html'
	#fill_sql_form = FillQueryForm()
	#custom_sql_form = CustomQueryForm()
	#dropdown_form = QueryDropdownForm()
	#map_form = MapForm()
	return render(request, template_name)
