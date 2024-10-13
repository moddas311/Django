from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE, GENDER_TYPE 

# Create your models here.
class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name = 'account', on_delete = models.CASCADE)
    account_no = models.IntegerField(unique=True) # account no duijon user er kokhono same hobe na
    account_type = models.CharField(max_length = 10, choices = ACCOUNT_TYPE)
    # account_number = models.IntegerField(unique = True) #account number must be unique.
    birth_date = models.DateField(null = True)
    gender = models.CharField(max_length = 10, choices = GENDER_TYPE)
    initial_deposit_date = models.DateField(auto_now_add = True)
    balance = models.DecimalField(default = 0, max_digits = 12, decimal_places = 2) #ekjon user 12 digits 
    # obdhi tk rakhte parbe, and doshomik er por 2 digits thakbe. (1000.23)
    
    def __str__(self):
        return str(self.account_no)
    
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name = 'address', on_delete = models.CASCADE)
    street_address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.user.email)
