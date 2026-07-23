from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from class_based_api.models import *
from class_based_api.serializers import *


class ClassBasedApiSerial(APIView):
    def get(self,request):

        student = StuInfoModel.objects.all()
        serializer = serializersStuModel(student, many = True)

        return Response({
            "success" : True,
            "message" : "Data get Successfully",
            "data" : serializer.data
        },status = status.HTTP_200_OK)
    

    def post(self,request):
        serializer = serializersStuModel(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success" : True,
                "message" : "data created",
                "data" : serializer.data
            },status = status.HTTP_201_CREATED)

        else:
            return Response({
                "success" : False,
                "message" : "Data invalid",
                "error" : serializer.errors
            },status = status.HTTP_400_BAD_REQUEST)



class ClassBasedApiIdTake(APIView):
    def get_object(request,id):
        try:
            students = get_object_or_404(StuInfoModel,id = id)
            return students
        except StuInfoModel.DoesNotExist:
            return Response({
                'success' : False,
                'message' : 'data dose not found',
            },status= status.HTTP_510_NOT_EXTENDED)

    def get(self,request,id):
        student = self.get_object(id)
        serializer = serializersStuModel(student)
        return Response({    
                "success" : True,
                "message" : "data get",
                "data" : serializer.data
        },status = status.HTTP_201_CREATED) 

    def put(self,request,id):
        student = self.get_object(id)
        serializer = serializersStuModel(student,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success' : True,
                'message' : 'working fucking task',
                'data' : serializer.data
            },status=status.HTTP_200_OK)

        else:
            return Response({
                'success' : False,
                'message' : 'dose not working fucking task',
                'error' : serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        student = self.get_object(id)
        student.delete()
        return Response({
            'success' : True,
            'message' : 'delete successfully'
        },status=status.HTTP_200_OK)



