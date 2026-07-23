from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from genericsApp.models import *
from genericsApp.serializers import *

class studentGenericslistApi(generics.ListCreateAPIView):
    queryset = StuInfoModel.objects.all()
    serializer_class = serializersStuModel

class studentGenericsDetailsApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = StuInfoModel.objects.all()
    serializer_class = serializersStuModel