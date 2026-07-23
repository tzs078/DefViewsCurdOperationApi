from django.urls import path
from serialApp.views import *
urlpatterns = [
    path('info_list/',info_list, name = 'info_list'),
    path('info_details/<str:id>/',info_details, name='info_details'),
    
]