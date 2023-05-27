from rest_framework import permissions 


class OwnProductPermission(permissions.BasePermission):
    message = 'you can\'t change others\' product :))'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not str(obj.owner) == str(request.user):
            return False
        return True
