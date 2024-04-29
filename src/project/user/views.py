from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User, Role, Permission
from .serializers import UserSerializers, RoleSerializers, PermissionSerializers


class UserListApiViews(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserDetailApiViews(APIView):
    def get(self,reqest, user_id, *args, **kwargs):
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request, user_id, *args, **kwargs):
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializers(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, user_id, *args, **kwargs):
        user = get_object_or_404(User, pk=user_id)
        user.delete()
        return Response({'message':'user deleted'}, status=status.HTTP_204_NO_CONTENT)
    


class RoliLIstApiViews(APIView):
    def get(self, request, *args, **kwargs):
        role = Role.objects.all()
        serializer = RoleSerializers(role, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = RoleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RoleDetailApiViews(APIView):
    def get(self,reqest, user_id, *args, **kwargs):
        role = get_object_or_404(Role, pk=user_id)
        serializer = RoleSerializers(role)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request, user_id, *args, **kwargs):
        role = get_object_or_404(Role, pk=user_id)
        serializer = RoleSerializers(instance=role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, user_id, *args, **kwargs):
        role = get_object_or_404(Role, pk=user_id)
        role.delete()
        return Response({'message':'user deleted'}, status=status.HTTP_204_NO_CONTENT)



class PermissionListApiViews(APIView):
    def get(self, request, *args, **kwargs):
        permission = Permission.objects.all()
        serializer = PermissionSerializers(permission, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = PermissionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PermissionDeatilApiViews(APIView):
    def get(self,reqest, pk, *args, **kwargs):
        permission = get_object_or_404(Permission, pk=pk)
        serializer = PermissionSerializers(permission)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk, *args, **kwargs):
        permission = get_object_or_404(Permission, pk=pk)
        serializer = PermissionSerializers(instance=permission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk, *args, **kwargs):
        permission = get_object_or_404(Permission, pk=pk)
        permission.delete()
        return Response({'message':'user deleted'}, status=status.HTTP_204_NO_CONTENT)
