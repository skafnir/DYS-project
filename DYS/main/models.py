from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=64, blank=True)
    street = models.CharField(max_length=64, blank=True)
    postal_code = models.CharField(max_length=5, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Numer musi być w formacie: '+999999999'. Do 15 cyfr.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class TypeOf(models.Model):
    name = models.CharField(max_length=64)


class Organization(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    type_of = models.ManyToManyField(TypeOf)


class Donation(models.Model):
    WHAT_THINGS = (
        (1, "ubrania, które nadają się do ponownego użycia"),
        (2, "ubrania, do wyrzucenia"),
        (3, "zabawki"),
        (4, "książki"),
        (4, "inne")
    )

    what_things = models.IntegerField(choices=WHAT_THINGS)
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
    type_of = models.ManyToManyField(TypeOf)

