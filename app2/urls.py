from django.urls import path
from app2.views import *
app_name='chaithanya'
urlpatterns=[
    path('index/',index ,name='index'),
    path('home/',home,name='home'),
    path('first/',first,name='first')
]