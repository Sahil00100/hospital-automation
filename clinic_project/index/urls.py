from django.urls import path,include
from.views import *
from django.conf import settings
import os
urlpatterns = [
   
   path('login/',login_view,name='login'),
   path('index/',middle_view,name='index'),
   path('new/',new_patient_view,name='new'),
   path('patient/',patient_login,name='patient'),
   path('view/<str:code>/',patient_view,name='view'),
   path('logout/',logout_view,name='logout'),
   path('result/<str:code>/',result,name='result'),
]