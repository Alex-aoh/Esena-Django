from rest_framework import serializers
from accounts.models import Account
class UsernameSerializer(serializers.Serializer):
   username = serializers.CharField()

class EmailSerializer(serializers.Serializer):
   email = serializers.CharField()

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'auth0user', 'first_name', 'last_name', 'gender', 'birthday', 'management_registered']

class SignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.CharField()
    birthday = serializers.DateField()
