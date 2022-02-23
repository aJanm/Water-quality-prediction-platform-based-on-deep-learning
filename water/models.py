from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province)
    city = models.CharField(max_length=50)


class Factory(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=25)
    date = models.CharField(max_length=50)
    ph = models.CharField(max_length=20)
    cod = models.CharField(max_length=20)
    nh4 = models.CharField(max_length=20)
    level = models.CharField(max_length=20)


# 此模型可以增加额外的属性
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username
