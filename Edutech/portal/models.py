from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from school.models import School


class UserAccountManager(BaseUserManager):
    def create_user(self, cell, username, address_line, email, password=None):
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(
            cell=cell,
            username=username,
            email=email,
            address=address_line,
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, cell, username, address_line, email, password=None):
        user = self.create_user(cell, username, address_line, email, password)
        user.is_superuser = True
        user.is_staff = True

        user.save()
        return user

    def create_service_provider(self, username, cell, address_line, email, password=None):
        user = self.create_user(username, email, address_line, cell, password)
        user.is_service_provide = True
        user.save()

        return user


class User(AbstractUser, PermissionsMixin):
    cell = models.CharField(max_length=10, unique=True, primary_key=False)
    address_line = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    username = models.CharField(max_length=250, unique=True)

    is_active = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'address_line']

    def __str__(self):
        return self.email


class Student(models.Model):
    first_name = models.ForeignKey(User.first_name, max_length=256)
    last_name = models.ForeignKey(User.last_name, max_length=256)
    address_line = models.ForeignKey(User.address_line)
    strengths = models.ManyToManyField()
    weaknesses = models.ManyToManyField()
    grade_or_form = models.IntegerField()
    sport = models.ManyToManyField()
    national_id = models.CharField(max_length=13)
    school = models.ForeignKey(School, related_name="learns")

    def __str__(self):
        return self.first_name and self.last_name


class Parent(models.Model):
    user = models.ForeignKey(User, related_name="users")
    address_line = models.ForeignKey(User.address_line)
    parent_to = models.ForeignKey(Student)
    cell = models.ManyToManyField(User.cell)
    national_id = models.CharField(max_length=13)
    school = models.ForeignKey(School, related_name="learns")

    def __str__(self):
        return self.user


class Portal(models.Model):
    pass
