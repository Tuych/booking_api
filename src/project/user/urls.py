from django.urls import path
from .views import UserListApiViews, UserDetailApiViews, RoliLIstApiViews, RoleDetailApiViews, PermissionListApiViews, PermissionDeatilApiViews
urlpatterns = [
    path('userList/', UserListApiViews.as_view()),
    path('userDetail/<int:user_id>/', UserDetailApiViews.as_view()),
    path('roleList/', RoliLIstApiViews.as_view()),
    path('roleDetail/<int:user_id>/', RoleDetailApiViews.as_view()),
    path('permissionList/', PermissionListApiViews.as_view()),
    path('permissionDetail/<int:pk>/', PermissionDeatilApiViews.as_view()),
]