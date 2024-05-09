from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User must have email ")
        if not username:
            raise ValueError("User must have username ")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using= self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,    
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    # Store the first name of the user, up to 50 characters long.
    first_name = models.CharField(max_length=50)
    # Store the last name of the user, up to 50 characters long.
    last_name = models.CharField(max_length=50)
    # Unique username for the user, up to 50 characters long.
    username = models.CharField(max_length=50, unique=True)
    # Unique email address for the user.
    email = models.EmailField(max_length=100, unique=True)
    # Phone number of the user, up to 12 characters long.
    phone_number = models.CharField(max_length=12)

    # Date and time when the account was created; set automatically when the account is created.
    date_joined = models.DateTimeField(auto_now_add=True)
    # Date and time of the user's last login; updated automatically at each login.
    last_login = models.DateTimeField(auto_now_add=True)
    # Boolean field indicating if the user has admin privileges.
    is_admin = models.BooleanField(default=False)
    # Boolean field indicating if the user can access the Django admin site.
    is_staff = models.BooleanField(default=False)
    # Boolean field indicating if the user's account is considered active.
    is_active = models.BooleanField(default=False)
    # Boolean field indicating if the user has superuser privileges (i.e., full permissions).
    is_superuser  = models.BooleanField(default=False)

    # Specifies the field to use as the unique identifier for a user when logging in.
    # In this case, the email field is used as the username for authentication.
    USERNAME_FIELD = 'email'

    # Specifies the additional fields required when creating a new user through the createsuperuser command.
    # These fields are required along with the username (email), such as first name, last name, and username.
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


    objects = MyAccountManager()


    # Return the email address when the Account object is printed.
    def __str__(self):
        return self.email

    # Check if the user has a specific permission; always True if the user is an admin.
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Check if the user has permissions to view the app `app_label`; always True for simplicity here.
    def has_module_perms(self, app_label):
        return True
