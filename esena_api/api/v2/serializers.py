from rest_framework import serializers
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'auth0user', 'first_name', 'last_name', "gender", "birthday", "management_registered"]