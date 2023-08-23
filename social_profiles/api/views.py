from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, exceptions, serializers, status
from rest_framework.response import Response
import time
from .serializers import SocialProfileSerializer
from social_profiles.models import SocialProfile


class MySocialProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return my socialProfile
        """ 
        sp = SocialProfile.objects.get(account=request.user.auth0user.account)
        serializer = SocialProfileSerializer(sp)
        

        return Response(serializer.data)
