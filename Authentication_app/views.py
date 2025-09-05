import random
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.mail import send_mail
from django.middleware.csrf import get_token
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import RegisterSerializer, VerifySerializer, LoginSerializer
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema 
import uuid

from django.shortcuts import render

def home(request):
    return render(request, "auth.html")

User = get_user_model()

def generate_otp():
    return "{:06d}".format(random.randint(0, 999999))

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(request_body=RegisterSerializer)         
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            if User.objects.filter(email=email).exists():
                return Response({"detail": "User already exists"}, status=400)
            otp = generate_otp()
            username = f"user_{uuid.uuid4().hex[:8]}"  

            user = User(username=username, email=email, is_active=False, is_verified=False, otp=otp)
            user.set_password(password)
            user.save()
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return Response({"detail": "OTP sent to email"}, status=201)
        return Response(serializer.errors, status=400)

class VerifyView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=VerifySerializer)         
    def post(self, request):
        serializer = VerifySerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'detail': 'User not found'}, status=404)
            if user.otp == otp:
                user.is_active = True
                user.is_verified = True
                user.otp = ''
                user.save()
                return Response({'detail': 'Email verified successfully'}, status=200)
            return Response({'detail': 'Invalid OTP'}, status=400)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(request_body=LoginSerializer)         
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"]
            )
            if user is not None and user.is_verified:
                login(request, user)
                resp = Response({"detail": "Logged in"}, status=200)
                resp.set_cookie(
                    'auth_token', request.session.session_key,
                    httponly=True, secure=True, samesite="Lax"
                )
                resp.set_cookie(
                    'csrftoken', get_token(request),
                    httponly=False, secure=True, samesite='Lax'
                )
                return resp
            return Response({"detail": "Invalid credentials or email not verified"}, status=400)
        return Response(serializer.errors, status=400)

class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "email": request.user.email,
            "username": request.user.username
        })

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        resp = Response({"detail": "Logged out"}, status=200)
        resp.delete_cookie('auth_token')
        return resp

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_csrf(request):
    return Response({'csrftoken': get_token(request)})
