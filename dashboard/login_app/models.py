from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    user_email = models.EmailField()
    designation = models.TextField(max_length=50, blank=True)
    Address = models.CharField(max_length=30, blank=True)
    mobile_no = models.IntegerField()

    def __str__(self):
        return self.user_email
