from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('dhoni finishes of is style')

def ms(request):
    return HttpResponse('chennai supper kings')