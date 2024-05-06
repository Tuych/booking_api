from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from project.user.models import User, Role, Permission
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer, RolePermissionSerializer
from project.api.v1.permissions import AdminPermission, IsStadiumOwner, IsAdminOrStadiumOwner


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminPermission]


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AdminPermission]



class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [AdminPermission]

class RolePermissionView(APIView):
    permission_classes = [AdminPermission]

    def patch(self, request, pk, *args, **kwargs):
        role = get_object_or_404(Role, id=pk)

        serializer = RolePermissionSerializer(role, data=request.data, partial=True)
        if serializer.is_valid():
            role.permission.set(serializer.validated_data['permission'])
            return Response(RoleSerializer(role).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



