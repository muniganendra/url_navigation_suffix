from django.urls import path
from app1.views import *
app_name='ganendra'

urlpatterns=[
    path('muni/',muni,name='muni'),
    path('venkey/',venkey,name='venkey'),

]