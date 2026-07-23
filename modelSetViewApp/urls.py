from django.urls import path,include
from modelSetViewApp.views import *
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register(r'students',ModelViewApi,basename='students')
urlpatterns = [
   path('',include(route.urls))
]