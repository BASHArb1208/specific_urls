from app4.views import *
from django.urls import path

app_name='rehan'

urlpatterns=[

    path('dhoni/',dhoni,name='dhoni'),
    path('ms/',ms,name='ms')
]