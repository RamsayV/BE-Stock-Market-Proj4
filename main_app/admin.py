from django.contrib import admin
from .models import Portfolio, Stock, Transaction
# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Stock)
admin.site.register(Transaction)