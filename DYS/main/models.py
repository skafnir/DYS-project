from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Needed?
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=5)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Numer musi być w formacie: '+999999999'. Do 15 cyfr.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class TypeOf(models.Model):
    name = models.CharField(max_length=64)


class Organization(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    type_of = models.ManyToManyField(TypeOf, on_delete=models.CASCADE)


class Donation(models.Model):
    what_things = models.CharField(max_length=64)
    amount = models.IntegerField()
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=5)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Numer musi być w formacie: '+999999999'. Do 15 cyfr.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    date = models.DateField()
    time = models.TimeField()
    extra_info = models.TextField(blank=True, null=True)
    type_of = models.ManyToManyField(TypeOf, on_delete=models.CASCADE)

