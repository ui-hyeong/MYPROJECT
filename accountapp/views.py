from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import newModel


def hello_cat(request):
    if request.method == 'POST':

        temp = request.POST.get('input_text')

        model_instance = newModel()
        model_instance.text = temp
        model_instance.save()

        return HttpResponseRedirect(reverse('accountapp:hello_cat'))  # 주소를 안쓰고 라우팅을 헤서 연결할 수있다.


    else:

        data_list = newModel.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_cat')
    template_name = 'accountapp/create.html'