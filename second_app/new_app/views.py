from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    page = {'contentPage':"This is coming from my index view"}
    return render(request, 'new_app/index.html', page)