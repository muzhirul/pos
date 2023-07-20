from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
from rest_framework_simplejwt.tokens import RefreshToken

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User must have an email address.')
        if not username:
            raise ValueError('User must have an username.')
        if not last_name:
            raise ValueError('User must have an last_name.')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



# def increment_cust_id():
#     max_cust_id = Account.objects.all().order_by('cust_id').last()
#     if not max_cust_id or max_cust_id.cust_id is None:
#         return


# Create your models here.
class Account(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,blank=False,null=False)
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    mobile = models.CharField(max_length = 100,blank=True, null = True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=50, unique=True,db_index=True)
    email = models.EmailField(max_length=255, unique=True,db_index=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['first_name', 'last_name','email']

    objects = MyAccountManager()

    class Meta:
        db_table = 'account'

    def __str__(self):
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
