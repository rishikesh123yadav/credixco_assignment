from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Student, Teacher, SuperAdmin
from .serializers import StudentSerializer, TeacherSerializer, SuperAdminSerializer
import jwt
from rest_framework.response import Response
from rest_framework import exceptions
from .serializers import StudentSerializer
from rest_framework.views import APIView
from django.conf import global_settings
# Create your views here

class AuthView(APIView):
    def post(self, request):
        id = request.data.get('id')
        password = request.data.get('password')
        if (id is None) or (password is None):
            raise exceptions.AuthenticationFailed(
                'id and password required')
        elif Student.objects.filter(id=id,password=password).exists():
            data = jwt.encode({'id': id, 'password': password}, key=global_settings.SECRET_KEY)
            return Response({'access_token': data})
        elif Teacher.objects.filter(id=id,password=password).exists():
            data = jwt.encode({'id': id, 'password': password}, key=global_settings.SECRET_KEY)
            return Response({'access_token': data})
        elif SuperAdmin.objects.filter(id=id,password=password).exists():
            data = jwt.encode({'id': id, 'password': password}, key=global_settings.SECRET_KEY)
            return Response({'access_token': data})
        else:
            return Response({'error': 'Id or Password wrong'})


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated, )



class TeacherCreate(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticated, )


class SuperAdminCreate(CreateAPIView):
    queryset = SuperAdmin.objects.all()
    serializer_class = SuperAdminSerializer
    permission_classes = (IsAuthenticated, )


class StudentDetails(APIView):
    permission_classes = (IsAuthenticated, )
    queryset = Student.objects.all()
    serializer_class = StudentSerializer