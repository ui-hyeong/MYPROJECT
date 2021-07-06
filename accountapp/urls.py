from django.urls import path

from accountapp.views import hello_cat

app_name = 'accountapp'

urlpatterns = [
    path('hello_cat/', hello_cat, name='hello_cat')
]