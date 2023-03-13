from app3.views import *
from django.urls import path

app_name='bashaaa'

urlpatterns=[

    path('blr/',blr,name='blr'),
    path('kar/',kar,name='kar')
]