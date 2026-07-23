from rest_framework import serializers
from serialApp.models import InfoModel

class infoModelSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoModel
        fields = '__all__'