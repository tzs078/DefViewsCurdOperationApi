from rest_framework import serializers
from class_based_api.models import *

class serializersStuModel(serializers.ModelSerializer):
    class Meta:
        model = StuInfoModel
        fields = '__all__'

       