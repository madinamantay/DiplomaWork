from django.contrib.auth.models import User, AbstractUser, \
    AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


# 3. Substitute by subclassing from AbstractUser

# class MyUserManager(UserManager):
#     def create_editor(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         extra_fields.setdefault('is_editor', True)
#         return self._create_user(username, email, password, **extra_fields)
#
#
# class MyUser(AbstractUser):
#     pass


# class Profile(models.Model):
#     user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
#     bio = models.TextField(default='')
#     address = models.TextField(default='')

# class Role(models.Model):
#     name = models.CharField(max_length=200)
#     # permissions
#
#
# class UserRole(models.Model):
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)


# a = MyUser.objects.create_editor(username='asd', email='asd@asd.asd', password='asd')


# 4. Substitute by subclassing from AbstractBaseUser
class MyAbstractUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField()

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        # abstract = True
        verbose_name = 'Renter'