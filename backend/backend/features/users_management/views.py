from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import Login, Profile, User
from .serializers import ProfileSerializer, UserSerializer
from datetime import datetime
import os

class LoginView(APIView):
    def new_login(self, user: User):
        Login.objects.create(
            user_id=user.id, 
            datetime=datetime.now(),
            location=self.request.META.get('REMOTE_ADDR'),
            app_version=os.environ.get('APP_VERSION')
        )
        
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            user = User.objects.get(email=email)
            if user is not None and check_password(password, user.password):
                self.new_login(user)
                refresh = RefreshToken.for_user(user)
                token = str(refresh.access_token)
                return Response({
                    'result': 'success',
                    'token': token
                    }, status=status.HTTP_200_OK
                )
            else:
                return Response({
                    'result': 'fail',
                    'detail': 'Invalid credentials'
                    }, status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            if str(e).__contains__('does not exist'):
                return Response({
                    'result': 'fail',
                    'detail': 'User not found'
                    }, status=status.HTTP_404_NOT_FOUND
                )
            return Response({
                'result': 'fail',
                'detail': str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CheckUserByEmail(APIView):
    def post(self, request):
        try:
            User.objects.get(
                email=request.data.get('email')
            )
            return Response({
                'result': 'success'
                }, status=status.HTTP_200_OK
            )
        except Exception as e:
            if str(e).__contains__('does not exist'):
                return Response({
                    'result': 'fail',
                    'detail': 'User not found'
                    }, status=status.HTTP_404_NOT_FOUND
                )
            return Response({
                'result': 'fail',
                'detail': str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class RecoverPassword(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            user = User.objects.get(email=email)
            user.password = 'XXXXXX'
            user.save()
            return Response({
                'result': 'success'
                }, status=status.HTTP_200_OK
            )
        except Exception as e:
            if str(e).__contains__('does not exist'):
                return Response({
                    'result': 'fail',
                    'detail': 'User not found'
                    }, status=status.HTTP_404_NOT_FOUND
                )
            return Response({
                'result': 'fail',
                'detail': str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )  

          
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        serializer.instance.token = token

        
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
