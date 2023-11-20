# Generated by Django 4.2.7 on 2023-11-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_stock_portfolios'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='portfolios',
            field=models.ManyToManyField(through='main_app.StockPortfolio', to='main_app.portfolio'),
        ),
    ]
