from django.shortcuts import render
from api.serializers import CoursesSerializer, StudentSerializer
from rest_framework import viewsets
from api.models import Courses, Student
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all().order_by("course_id")
    serializer_class = CoursesSerializer

    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        try:
            courses = Courses.objects.get(pk=pk)
            students = Student.objects.filter(courses=courses)
            stu_serializer = StudentSerializer(students, many=True, context={'request':request})
            res_msg = {'msg':'All students enrolled in part. course are retrieved!'}
            return Response({'data': stu_serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            res_msg = {'msg': 'Requested query matching courses doesnot exist!'}
            return Response(res_msg, status=status.HTTP_400_BAD_REQUEST)



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by("stu_id")
    serializer_class = StudentSerializer
