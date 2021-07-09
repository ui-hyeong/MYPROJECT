from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_cat(request):
    if request == 'POST':
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD'}) #alt enter를 통해 import를 해줄수 있음
    else:
        return render(request, 'accountapp/hello_world.html', context= {'text':'get method'})