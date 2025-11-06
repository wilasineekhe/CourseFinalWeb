from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Homepage(request):
    return render(request, 'general_APP/general_home.html')