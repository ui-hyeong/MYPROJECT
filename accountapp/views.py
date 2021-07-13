from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import newModel


def hello_cat(request):
    if request.method == 'POST':

        temp = request.POST.get('input_text')

        model_instance = newModel()
        model_instance.text = temp
        model_instance.save()

        return HttpResponseRedirect(reverse('accountapp:hello_cat'))


    else:

        data_list = newModel.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})