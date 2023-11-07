from django.shortcuts import render
from django.http import HttpResponse

#View: Describes which data is sent to the user but not its presentation

# Create your views here.
def homePageView(request):
    return HttpResponse("main page")