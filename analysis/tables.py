import django_tables2 as tables
from .models import SaveTable

class DataTable(tables.Table):
	class Meta:
		model = SaveTable
