from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('first/',first, name='first'),
    path('second/',second ,name='second'),
    path('index/',index,name='index'),
]