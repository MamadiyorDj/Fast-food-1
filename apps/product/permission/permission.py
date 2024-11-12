from rest_framework import permissions
from rest_framework.permissions import *


class MyUserPermissions(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.user == request.user