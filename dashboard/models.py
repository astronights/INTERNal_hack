from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200, default='')
    
class StockPrice(models.Model):
    company_name = models.OneToOneField(Company, on_delete=models.CASCADE)
    open_price = models.DecimalField(max_digits=9, decimal_places=2)
    close_price = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField()

class Score(models.Model):
    company_name = models.CharField(max_length=200, default='')
    sentiment_score = models.DecimalField(max_digits=8, decimal_places=3)
    date = models.DateField()

