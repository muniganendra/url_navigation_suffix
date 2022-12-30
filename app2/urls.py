from django.urls import path
from app2.views import *
app_name='nagaram'

urlpatterns=[
    path('muni/',muni,name='muni'),
    path('venkey/',venkey,name='venkey'),
]