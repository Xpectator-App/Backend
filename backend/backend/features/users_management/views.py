from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
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

            user = User.objects.get(email=email, password=password)
            if user is not None:
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
            return Response({
                'result': 'fail',
                'detail': str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CheckUserByEmail(APIView):
    def post(self, request):
        try:
            user = User.objects.get(
                email=request.data.get('email'))
            if user is not None:
                return Response({
                    'result': 'success'
                    }, status=status.HTTP_200_OK
                )
            else:
                return Response({
                    'result': 'fail'
                    }, status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
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



