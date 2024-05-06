from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin





class Permission(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=20, unique=True, null=False, blank=False)
    
    def __str__(self) -> str:
        return "%s - %s" % (self.name, self.code_name)
    



class Role(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=20, unique=True, null=False, blank=False)
    permission = models.ManyToManyField(Permission)

    def __str__(self) -> str:
        return "%s - %s" % (self.name, self.code_name)





class MyUserManager(BaseUserManager):

    def create_user(self, phone_number, password=None):
        user = self.model(
            phone_number=phone_number
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_number, password=None):
        user = self.create_user(phone_number=phone_number, password=password)
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=13, null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)  # is_staff
    joined_date = models.DateField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True )


    objects = MyUserManager()
    USERNAME_FIELD = 'phone_number'


    def __str__(self):
        return self.phone_number
    

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_superuser