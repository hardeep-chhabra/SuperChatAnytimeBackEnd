from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE



class RegisterUser(models.Model):
    profile_pic_url = models.CharField(max_length=500, null=True)
    user_id = models.OneToOneField(User, on_delete=CASCADE, null=True)