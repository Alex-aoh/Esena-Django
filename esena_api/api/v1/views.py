from rest_framework import viewsets, permissions, exceptions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UsernameSerializer, EmailSerializer

from common.exceptions import ServiceUnavailable
from .services import username_check_available, email_check_available

class UsernamesCheckAvailable(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = UsernameSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            try:
                check_result = username_check_available(username=username)
            except ServiceUnavailable:
                raise ServiceUnavailable(detail="Can't check the username availability, try again later.")
            else:
                return Response({"username": username, "used": check_result})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

class EmailsCheckAvailable(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                check_result = email_check_available(email=email)
            except ServiceUnavailable:
                raise ServiceUnavailable(detail="Can't check the email availability, try again later.")
            else:
                return Response({"email": email, "used": check_result})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
