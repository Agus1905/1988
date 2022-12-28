from django.shortcuts import render
from django.http import HttpResponse

from familiares.models import Familiares

def data_familiares(request):
    Familiares.data.all()
    print(all_Familiares)
    return HttpResponse("familiares")
    