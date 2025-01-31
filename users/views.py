from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer
import firebase_admin
from firebase_admin import auth as firebase_auth

class RegisterView(generics.GenericAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

      

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        
        firebase_user = firebase_aauth.create_user(uid=str(user.id))
        firebase_token = firebase_auth.create_custom_token(firebase_user.uid)
        
        
        return Response({
            'access_token': access_token,
            'refresh_token': str(refresh),
            'firebase_token': firebase_token
            
        }, status=status.HTTP_201_CREATED)
                        
                        
