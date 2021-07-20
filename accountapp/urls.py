from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_cat, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_cat/', hello_cat, name='hello_cat'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),  # loginview는 장고에서 제공해주는 클래스

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),

    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),  # pk라는 이름에 숫자를 받는다. pirmary key

    path('update/<int:pk>', AccountUpdateView.as_view(), name='update')

]