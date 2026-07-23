
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('serialApp.urls')),
    path('api/',include('class_based_api.urls')),
    path('api/',include('genericsApp.urls')),
    path('api/',include('modelSetViewApp.urls')),
]
