from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio_name = models.CharField(max_length=255, default='My Portfolio')
    total_value = models.DecimalField(max_digits=10, decimal_places=2)

    # def update_total_value(self):
    #     self.total_value = self.stockportfolio_set.aggregate(
    #         total=Sum(F('quantity') * F('stock__market_price'))
    #     )['total'] or 0
    #     self.save()

    def __str__(self):
        return f"{self.portfolio_name}"

class Stock(models.Model):
    ticker_symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=255)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    open_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    close_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    week_52_high = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    week_52_low = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    portfolios = models.ManyToManyField(Portfolio, through='StockPortfolio')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ticker_symbol} - {self.company_name}"

class Transaction(models.Model):
    BUY = 'buy'
    SELL = 'sell'
    TRANSACTION_TYPE_CHOICES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]

    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.IntegerField()
    price_at_transaction = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_fee = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    date = models.DateTimeField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)



class StockPortfolio(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    quantity = models.IntegerField()  
    class Meta:
        unique_together = ('stock', 'portfolio') 

    def __str__(self):
        return f"{self.quantity} shares of {self.stock} in {self.portfolio}"
    
 
