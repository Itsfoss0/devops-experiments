#!/usr/bin/env python3

""" Register the models on the admin UI """

from django.contrib import admin

from api.models import Student, SubjectGrade

admin.site.register(Student)
admin.site.register(SubjectGrade)
