from  rest_framework import  serializers
from .models import Teacher,Student,SuperAdmin

class SuperAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperAdmin
        fields = ('id', 'admin_firstname', 'admin_lastname', 'admin_email', 'admin_address', 'admin_phone', 'adminPass')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        student = Student(**validated_data)
        student.studentPass=password
        student.save()
        return student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'teacher_firstname','teacher_lastname','teacher_email',
                  'teacher_address','teacher_phone','creator_adminId','teacherPass')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        student = Student(**validated_data)
        student.studentPass=password
        student.save()
        return student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'student_firstname','student_lastname','student_email',
                  'student_address','student_phone','creator_Id','create_by','studentPass')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        student = Student(**validated_data)
        student.studentPass=password
        student.save()
        return student

