
from django.urls import path
from . import views

app_name = 'pluginServer'

urlpatterns=[
    path('plugin-list/',views.plugin_list,name='plugin-list'),
]
