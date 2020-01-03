from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, generics, status
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = TokenSerializer(data={
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(
            data={
                "error_code": 1,
                "message": "Не правильный логин или пароль"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )


class RegisterUsersView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        # print(username)
        # print(password)
        # print(email)
        if not username or not password or not email:
            return Response(
                data={
                    "error_code": 1,
                    "message": "Заполните все поля"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            new_user = User.objects.create_user(
                username=username, password=password, email=email
            )
        except IntegrityError:
            # print(IntegrityError)
            return Response(
                data={
                    "error_code": 2,
                    "message": "Пользователь с таким логином или email уже существует"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        new_profile = Profile.objects.create(user=User.objects.get(username=username))
        return Response(
            data={
                "username": username,
                "email": email
            },
            status=status.HTTP_201_CREATED
        )


class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()


class ProfileRudView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Profile.objects.all()


class ProfileGetByUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'user'

    def get_queryset(self):
        return Profile.objects.all()


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class GetUserByTokenView(APIView):

    def post(self, request):
        data = {'token': request.data['token']}
        try:
            valid_data = VerifyJSONWebTokenSerializer().validate(data)
            user = {
                'id': valid_data['user'].id,
                'username': valid_data['user'].username,
                'email': valid_data['user'].email
            }
        except ValidationError:
            return Response(
                data={
                    "error_code": 1,
                    "message": "Пользователь не найден"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response({'user': user})


class TimerTypeCreateView(generics.CreateAPIView):
    serializer_class = TimerTypeSerializer

    def get_queryset(self):
        return TimerType.objects.all()


class TimerTypeRudView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TimerTypeSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return TimerType.objects.all()


class TimerTypeListView(generics.ListAPIView):
    serializer_class = TimerTypeSerializer

    def get_queryset(self):
        return TimerType.objects.all()


class TimerCreateView(generics.CreateAPIView):
    serializer_class = TimerSerializer

    def get_queryset(self):
        return Timer.objects.all()


class TimerRudView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TimerSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Timer.objects.all()


class TimerListView(generics.ListAPIView):
    serializer_class = TimerSerializer

    def get_queryset(self):
        return Timer.objects.all()


class SubjectCreateView(generics.CreateAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return Subject.objects.all()


class SubjectRudView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Subject.objects.all()


class SubjectListView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return Subject.objects.all()