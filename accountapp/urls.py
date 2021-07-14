from django.urls import path

from accountapp.views import hello_cat, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_cat/', hello_cat, name='hello_cat'),
    path('create/', AccountCreateView.as_view(), name='create')
]