from django.db import models
import re


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        all_users = User.objects.all()
        for user in all_users:
            if postData['email'].upper() == user.email.upper():
                errors['duplicate'] = "Email already exists"
        if len(postData['fname']) < 2 or not postData['fname'].isalpha() :
            errors['fname'] = "First Name should be at least 2 characters and only contains letters"
        if len(postData['lname']) < 2 or not postData['lname'].isalpha():
            errors['lname'] = "Last name should be at least 3 characters and only contains letters"
        EMAIL_REGEX = re.compile(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$")
        if not EMAIL_REGEX.match(postData['email']):
            errors['invalid_email'] = "Invalid email address"
        if len(postData['pass']) < 8 or len(postData['passconfirm']) < 8:
            errors['passlength'] = "Password needs to be at least 8 characters"
        if postData['pass'] != postData['passconfirm'] :
            errors['passconfirm'] = "Password and Confirm Password must match"
        return errors


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
