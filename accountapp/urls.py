from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_cat, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_cat/', hello_cat, name='hello_cat'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),  # loginview는 장고에서 제공해주는 클래스

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create')

]