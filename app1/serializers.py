from app1.models import *
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

class EmployeSerializers(serializers.ModelSerializer):
    student_name=serializers.CharField(source='student.name',read_only=True)
    student_data=StudentSerializers(source='student',read_only=True)
    class Meta:
        model=Employee
        fields='__all__'