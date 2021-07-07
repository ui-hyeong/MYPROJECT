from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_cat(request):
    return render(request, 'accountapp/hello_world.html') #alt enter를 통해 import를 해줄수 있음