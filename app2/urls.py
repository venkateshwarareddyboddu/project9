from app2.views import *
from django.urls import path 
app_name='something'
urlpatterns=[
    path ('sample2/',sample2,name='sample2'),

]