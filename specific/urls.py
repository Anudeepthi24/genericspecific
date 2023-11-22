from specific.views import * 
from django.urls import path

app_name='nothing'

urlpatterns=[
    path('anu/',anu,name='anu'),
    path('sai/',sai,name='sai'),


]