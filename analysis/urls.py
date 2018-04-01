from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^your-custom-query/', views.get_custom_query),
    url(r'^your-selection/', views.get_selection),
    url(r'^your-query/', views.test_query),
    url(r'^map/', views.get_map),
    url(r'^save/',views.save_query,name='save'),
]

# change get_query to test_query
