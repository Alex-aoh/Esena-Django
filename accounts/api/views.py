from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, exceptions, serializers, status
from rest_framework.response import Response

from .serializers import AccountSerializer, CreateAccountSerializer, AccountDepthSerializer
from accounts.models import Account

import time

class MyAccount(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return my account
        """
        try:
            account = Account.objects.get(auth0user= request.user.auth0user)
        except Exception:
            raise exceptions.NotFound(detail="No Account Created")
        else:
            serializer = AccountDepthSerializer(account)
            time.sleep(1)
            return Response(serializer.data)
    def post(self, request, format=None):
        """
        Create account
        """
        serializer = CreateAccountSerializer(data=request.data)
        if serializer.is_valid():
            account, created = Account.objects.get_or_create(auth0user=request.user.auth0user)
            account.first_name = serializer.validated_data['first_name']
            account.last_name = serializer.validated_data['last_name']
            account.gender = serializer.validated_data['gender']
            account.birthday = serializer.validated_data['birthday']
            account.save()
            return Response(AccountSerializer(account).data)
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, format=None):
        """
        Create account
        """
        serializer = CreateAccountSerializer(data=request.data)
        if serializer.is_valid():
            account, created = Account.objects.get_or_create(auth0user=request.user.auth0user)
            account.first_name = serializer.validated_data['first_name']
            account.last_name = serializer.validated_data['last_name']
            account.gender = serializer.validated_data['gender']
            account.birthday = serializer.validated_data['birthday']
            account.save()
            return Response(AccountSerializer(account).data)
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)