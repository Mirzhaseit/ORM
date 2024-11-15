from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin

class BankLoan(models.Model):
    CustomerName = models.CharField(max_length=50)
    LoanNumber = models.IntegerField(primary_key=True)
    LoanAmount = models.DecimalField(max_digits=15, decimal_places=2)
    InterestRate = models.FloatField()
    LoanStartDate = models.DateField()
    Email = models.EmailField()

class BankLoanAdmin(admin.ModelAdmin):
    list_display = ('CustomerName', 'LoanNumber', 'LoanAmount', 'InterestRate', 'LoanStartDate', 'Email')
