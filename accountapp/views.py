from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
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

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

has_ownership = [login_required, account_ownership_required] # 두가지 decorate를 적용시켜준다.

@method_decorator(has_ownership, 'get')  #함수에 쓰일 데코레이터를 메서드에도 적용시킨다. login을 어디에 적용시킬지도 작성해야한다.
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_cat')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')  #함수에 쓰일 데코레이터를 메서드에도 적용시킨다. login을 어디에 적용시킬지도 작성해야한다.
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_cat')
    template_name = 'accountapp/delete.html'
