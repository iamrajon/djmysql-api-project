from rest_framework import serializers
from api.models import Courses, Student


# Serializer for Courses Model
class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    course_id = serializers.ReadOnlyField()
    class Meta:
        model = Courses
        fields = '__all__'



# Serializer for Student Model
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    stu_id = serializers.ReadOnlyField()
    class Meta:
        model = Student
        fields = '__all__'