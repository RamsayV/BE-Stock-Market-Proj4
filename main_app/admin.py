from django.contrib import admin
from .models import Portfolio, Stock, Transaction,StockPortfolio
# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Stock)
admin.site.register(Transaction)
admin.site.register(StockPortfolio)