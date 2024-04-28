from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Role(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return "%s - %s" %(self.name, self.code_name)


class Permission(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=20, unique=True, null=False, blank=False)
    role = models.ManyToManyField(Role)
    

    def __str__(self) -> str:
        return "%s - %s" %(self.name, self.code_name)


class UserManager(BaseUserManager):

    def create_user(self, username, password):
        user = self.model(
            username=username,
            
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=30,unique=True,null=False)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)  # is_staff
    joined_date = models.DateField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True )


    objects = UserManager()
    USERNAME_FIELD = 'username'


    def __str__(self) -> str:
        return "%s - %s" % (self.first_name, self.last_name)
    

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_superuser