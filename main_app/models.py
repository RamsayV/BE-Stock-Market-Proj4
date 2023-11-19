from django.db import models
from django.contrib.auth.models import User



class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)

class Stock(models.Model):
    ticker_symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=255)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    portfolios = models.ManyToManyField(Portfolio)

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=4, choices=[('buy', 'Buy'), ('sell', 'Sell')])
    amount = models.IntegerField()
    price_at_transaction = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


