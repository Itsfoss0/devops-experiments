#!/usr/bin/env python3

""" URL configurations for the api """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    PingAPI,
    StudentList,
    StudentDetailView
)

router = DefaultRouter()
router.register('', StudentList)


urlpatterns = [
    path('status/', PingAPI.as_view(), name='status'),
    path('students/', include(router.urls)),
    path('student/<uuid:id>', StudentDetailView.as_view(), name='student-detail')
]


