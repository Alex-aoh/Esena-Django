from rest_framework.permissions import BasePermission
from .authentication import is_valid_auth0token
from rest_framework import exceptions


class HasPermission(BasePermission):
    permission = None

    """
    User is allowed access if has the expected permission
    """
    def has_permission(self, request, view):
        payload, is_valid = is_valid_auth0token(request.auth)
        if not is_valid:
            raise exceptions.AuthenticationFailed(self.err_msg)
        print(payload)
        return self.permission in payload['permissions']

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class HasAdminPermission(HasPermission):
    permission = "read:admin-messages"

class HasUsersPermission(HasPermission):
    permission = "read:users"