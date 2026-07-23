from django.urls import path
from genericsApp.views import *
urlpatterns = [
   path('student/',studentGenericslistApi.as_view(),name='studentlist'),
   path('student/<str:pk>/',studentGenericsDetailsApi.as_view(),name='studentcreat'),
]