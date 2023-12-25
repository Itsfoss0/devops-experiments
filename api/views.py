#!/usr/bin/env python3

""" Views for the api """

from django.utils import timezone

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status

from api.models import Student
from api.serializers import StudentModelSerialzer


class PingAPI(APIView):

    def get(self, request):
        message = {
            "status": "OK",
            "today": timezone.now()
        }
        return Response(message)


class StudentList(ModelViewSet):
    serializer_class = StudentModelSerialzer
    queryset = Student.objects.all()


class StudentDetailView(APIView):
    def get_student(self, id):
        try:
            student = Student.objects.get(id=id)
            return student
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id, format=None):
        student_instance = self.get_student(id=id)
        serializer = StudentModelSerialzer(student_instance)
        return Response(data={
            "message": "success",
            "data": serializer.data
        })

    def delete(self, request, id, format=None):
        student_instance = self.get_student(id=id)
        if student:
            student_instance.delete()
            return Response(
                data={"message": "Deleted", },
                status=status.HTTP_204_NO_CONTENT
            )

    def put(self, request, id, format=None):
        student_instance = self.get_object(id=id)
        serializer = StudentModelSerializer(
            student_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "message": "success",
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
