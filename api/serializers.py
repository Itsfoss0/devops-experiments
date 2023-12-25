#!/usr/bin/env python3

""" Serializer """


from rest_framework.serializers import ModelSerializer

from api.models import (
    Student,
    SubjectGrade
)


class GradesSerializer(ModelSerializer):
    class Meta:
        model = SubjectGrade
        fields = ('subject', 'grade')


class StudentModelSerialzer(ModelSerializer):
    grades = GradesSerializer(many=True, source='stud_grades')

    class Meta:
        model = Student
        fields = ('f_name', 'grades', 'reg_no', 'id')
