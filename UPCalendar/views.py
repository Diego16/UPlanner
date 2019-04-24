from django.shortcuts import render
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


from UPCalendar.models import Student, Event
from UPCalendar.serializers import StudentSerializer, CreateUserSerializer, CreateEventSerializer, EventSerializer, UserSerializer, LoginUserSerializer


class RegistrationAPI(generics.GenericAPIView):

    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):

    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class StudentsAPI(APIView):

    def get(self, request):
        students = Student.objects.all()
        serialized = StudentSerializer(students, many=True)
        return Response(serialized.data)


class EventsAPI(APIView):

    serializer_class = EventSerializer

    def get(self, request):
        data = Event.objects.all()
        serialized = EventSerializer(data, many=True)
        return Response(serialized.data)


class CreateEventAPI(generics.GenericAPIView):
    serializer_class = CreateEventSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = serializer.save()
        return Response({
            'id': EventSerializer(event, context=self.get_serializer_context()).data,
            'title': EventSerializer(event, context=self.get_serializer_context()).data,
            'start': EventSerializer(event, context=self.get_serializer_context()).data,
            'end': EventSerializer(event, context=self.get_serializer_context()).data
        })
