from rest_framework import serializers
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'gender', 'birthday', 'management_registered', 'social_profiles']

class CreateAccountSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.CharField()
    birthday = serializers.DateTimeField()

class AccountDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'gender', 'birthday', 'management_registered', 'social_profiles']
        depth = 1