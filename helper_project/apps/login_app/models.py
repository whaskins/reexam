from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def validate(self, data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = {}
        if len(data.get('first_name')) < 3:
            errors['first_name'] = "First Name must be at least 3 chars"
        if len(data.get('last_name')) < 3:
            errors['last_name'] = "Last Name must be at least 3 chars"
        if len(data.get('password')) < 8:
            errors['password'] = "Password must be at least 8 chars"
        if not EMAIL_REGEX.match(data.get('email')):
            errors['email'] = "Please enter a valid email address"
        if len(User.objects.filter(email=data.get('email'))) > 0:
            errors['email'] = "Email already registered"
        if data.get('password') != data.get('confpword'):
            errors['confpword'] = "Passwords don't match"
        return errors

    def validateEmail(self, data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(data.get('password')) < 8:
            errors['password'] = "Password must be at least 8 chars"
        if not EMAIL_REGEX.match(data.get('email')):
            errors['email'] = "Please enter a valid email address"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()