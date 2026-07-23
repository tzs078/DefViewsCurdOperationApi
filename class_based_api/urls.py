from django.urls import path
from class_based_api.views import *
urlpatterns = [
    path('ClassBasedApiSerial/',ClassBasedApiSerial.as_view(),name='ClassBasedApiSerial'),
    path('ClassBasedApiIdTake/<str:id>/',ClassBasedApiIdTake.as_view(),name='ClassBasedApiIdTake'),
    
]