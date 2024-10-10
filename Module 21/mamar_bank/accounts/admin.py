from django.contrib import admin
from .models import userBankAccount, userAddress

# Register your models here.
admin.site.register(userBankAccount)
admin.site.register(userAddress)