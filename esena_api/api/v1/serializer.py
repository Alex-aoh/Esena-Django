from rest_framework import serializers

class UsernameSerializer(serializers.Serializer):
   username = serializers.CharField()

class EmailSerializer(serializers.Serializer):
   email = serializers.CharField()