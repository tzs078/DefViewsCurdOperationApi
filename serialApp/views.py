from rest_framework.decorators import api_view
from rest_framework.response import Response
from serialApp.models import InfoModel
from serialApp.serializers import infoModelSerial
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def info_list(request):
    if request.method == 'GET':
        infos = InfoModel.objects.all()
        serializer = infoModelSerial(infos ,many = True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = infoModelSerial(data =  request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT', 'DELETE'])

def info_details(request,id):
    try:
        info = InfoModel.objects.get(id = id)

    except InfoModel.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = infoModelSerial(info)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = infoModelSerial(info, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

