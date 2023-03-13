from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blr(request):
    return HttpResponse("silicon city") 

def kar(request):
    return HttpResponse('clean and green city')
