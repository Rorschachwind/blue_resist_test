# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import inspect
from .forms import CustomQueryForm, QueryDropdownForm, FillQueryForm, MapForm
from .models import QueryDropdown
from django.db import connection
import xlwt
import csv

query_dict = {'1':'SELECT site_id, cfu, ctx FROM plate JOIN agar ON plate.agar_id = agar.agar_id', '2':'two'}

def index(request): # GET
	# create blank forms
	template_name = 'analysis/index.html'
	fill_sql_form = FillQueryForm()
	custom_sql_form = CustomQueryForm()
	dropdown_form = QueryDropdownForm()
	map_form = MapForm()
	return render(request, template_name, {'custom_sql_form': custom_sql_form, 'dropdown_form': dropdown_form, 'fill_sql_form':fill_sql_form, 'map_form':map_form})

# CUSTOM SQL
def get_custom_query(request): # POST
	# create a form instance and populate it with data from the request
	sql_form = CustomQueryForm(request.POST)
	# check if it's valid
	if sql_form.is_valid(): 
		# process the data in form.cleaned_data as required
		query = sql_form.cleaned_data['query']

		try:
			result = execute_query(query)
			colnames = result[0].keys
			num_rows = len(result)
			return render(request, 'analysis/query.html', {'query':query, 'num_rows':num_rows, 'result':result, 'colnames':colnames})
		except: 
			return HttpResponse("There were one or more errors in your query. Please try again.")
	else:
		return HttpResponse("Could not execute query.")

# DROPDOWN
def get_selection(request):
	dropdown_form = QueryDropdownForm(request.POST)
	if dropdown_form.is_valid():
		query_num = dropdown_form.cleaned_data['query']
		query = query_dict[query_num]
		result = execute_query(query)
		colnames = result[0].keys
		num_rows = len(result)
		# return BarView.as_view()
		return render(request, 'analysis/query.html', {'query':query, 'num_rows':num_rows, 'result':result, 'colnames':colnames, 'preselected':True})
	else:
		return HttpResponse("Could not execute selection.")

# FILL IN SQL
def get_query(request):
	sql_form = FillQueryForm(request.POST)
	if sql_form.is_valid(): 
		# process the data in form.cleaned_data as required
		select = sql_form.cleaned_data['select']
		from_field = sql_form.cleaned_data['from_field']
		where = sql_form.cleaned_data['where']
		limit = sql_form.cleaned_data['limit']
		query = 'SELECT ' + select + ' FROM ' + from_field + ' WHERE ' + where + ' LIMIT ' + limit
		try:
			result = execute_query(query)
			colnames = result[0].keys
			num_rows = len(result)
			return render(request, 'analysis/your-query.html', {'query':query, 'num_rows':num_rows, 'result':result, 'colnames':colnames})
		except:
			return HttpResponse("There were one or more errors????????? in your query. Please try again.")
	else:
		return HttpResponse("Could not execute query.")

#test_query
def test_query(request):
	 ID ='7'
         media = 'mac'
	 temp = 'rt'
	 ctx = '0'
         sql_form=FillQueryForm(request.POST)
         if sql_form.is_valid():
                 select = sql_form.cleaned_data['select']
#                 result = execute_query(select)
                 from_field = sql_form.cleaned_data['from_field']
                 where = sql_form.cleaned_data['where']
                 limit = sql_form.cleaned_data['limit']
                 query = {'SELECT':[select], 'FROM':[from_field], 'WHERE':[where], 'LIMIT':[limit]}
		
		#add a new test data to csv file
		result = []#creat empty list for showing on web
		 with open('/home/xp14/Blue_project/blue_resist_test/data/%s.csv'%(from_field)) as csvfile:
    			reader = csv.DictReader(csvfile)
    			fieldnames = reader.fieldnames
			# create a new csv file and write content
    			with open('/home/xp14/Blue_project/blue_resist_test/data/new_test.csv','a') as newfile:
				newwriter = csv.DictWriter(newfile,fieldnames=fieldnames)
				newwriter.writeheader()
        			for row in reader:
					result.append(row)
					newwriter.writerow(row)
        			newfile.close()
				
#		 with open('/home/xp14/Blue_project/blue_resist_test/data/%s.csv'%(from_field),'a') as csvfile:  
#    			csvfile.write('\n')
#    			csvfile.close()
    
		 with open('/home/xp14/Blue_project/blue_resist_test/data/%s.csv'%(from_field),'a') as csvfile:   
#    fieldnames = ['Agar_ID','Media','Temp','CTX']
    			spamwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
#    spamwriter.writeheader() #this will add the fieldname as title again

# add new info
    		 	spamwriter.writerow({'Agar_ID':'%s'%(ID),'Media':'%s'%(media),'Temp':'%s'%(temp),'CTX':'%s'%(ctx)})
    			csvfile.close()

# save to a new xls (maybe no use)
#                 book = xlwt.Workbook()
#                 sheet1 = book.add_sheet('test666')
#                 row = 0
#                 col = 0
#                 for key in query.keys():
#                     row += 1
#                     sheet1.write(row,col,key)
#                     for item in query[key]:
#                         sheet1.write(row,col+1,item)
#                         row += 1
#                 book.save('output.xls')


#                 query = 'SELECT ' + select + ' FROM ' + from_field + ' WHERE ' + where + ' LIMIT ' + limit
                 try:
#                        result = execute_query(query)
#                        result = [{'parent_id': None, 'id': 54360982}, {'parent_id': None, 'id': 54360880}]#a test example
                        colnames = result[0].keys
                        num_rows = len(result)
#                        return render(request, 'analysis/your-query.html', {'query':'abcde', 'num_rows':'5', 'result':'2345', 'colnames':'23333'})
         
#         result=[{'parent_id': None, 'id': 54360982}, {'parent_id': None, 'id': 54360880}]
#         colnames = result[0].keys
#         num_rows = len(result)
                        return render(request, 'analysis/your-query.html', {'num_rows':num_rows, 'result':result, 'colnames':colnames})
                 except:
                        return HttpResponse("There were one or more errors????????? in your query. Please try again.")
#         else:
#                return HttpResponse("Could not execute query.")
#         query=str(sql_form)
#         return render(request,'analysis/your-query.html',{'colnames':'233333'})
        
# GOOGLE MAP 
def get_map(request):
	return render(request, 'analysis/map.html')

def execute_query(query):
	with connection.cursor() as cursor:
		cursor.execute(query)
		return dictfetchall(cursor)
	# ex: [{'parent_id': None, 'id': 54360982}, {'parent_id': None, 'id': 54360880}]

def dictfetchall(cursor):
	# Return all rows from a cursor as a dict
	columns = [col[0] for col in cursor.description]
	return [
    	dict(zip(columns, row))
    	for row in cursor.fetchall()
    ]

