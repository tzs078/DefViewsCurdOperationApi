from django.urls import path
from class_based_api.views import *
urlpatterns = [
    path('students/',ClassBasedApiSerial.as_view(),name='studentList'),
    path('students/<str:id>/',ClassBasedApiIdTake.as_view(),name='studentDetails'),
    
]