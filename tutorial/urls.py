from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^about/',views.about),
    url(r'^learn/',views.learn),
    url(r'^contribute/',views.contribute),
    url(r'^run_vm/',views.run_vm,name = 'runvm'),
    url(r'^tool_install/',views.tool_install,name = 'install'),
]
