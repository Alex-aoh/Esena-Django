from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Account
from .serializers import AccountSerializer
from authz import permissions

# --- Accounts Related Views ---

class AccountViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]