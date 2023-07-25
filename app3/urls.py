from django.urls import path
from app3.views import *
app_name='divaysree'
urlpatterns=[
    path('chaithu/',chaithu,name='chaithu'),
    path('divya/',divya,name='divya'),
    path('string/',string,name='string')
]