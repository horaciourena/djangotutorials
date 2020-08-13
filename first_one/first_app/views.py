from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    my_diccionary = {'inser_me':"Now I'm comming from first_app/index.html linked with views.py !"}
    return render(request, 'first_app/index.html', my_diccionary)

def getDate(request):
    currentDate = datetime.datetime.now()

    outputDate = "La fecha y hora actual es %s" % currentDate

    return HttpResponse(outputDate)

def calculateAge(request, age, year):

    period = year - 2020
    futureAge = age + period
    outputAge = "En el Año %s tu edad sera: %s años" %(year, futureAge)

    return HttpResponse(outputAge)