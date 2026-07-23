from modelSetViewApp.serializers import *
from modelSetViewApp.models import *
from rest_framework.viewsets import ModelViewSet

class ModelViewApi(ModelViewSet):
    queryset = StuInfoModel.objects.all()
    serializer_class = serializersStuModel
    