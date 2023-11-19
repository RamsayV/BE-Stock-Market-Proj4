from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Portfolio, Stock, Transaction

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username','email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'username']

class PortfolioSerializer(serializers.ModelSerializer):
    user = UserSerializer()  

    class Meta:
        model = Portfolio
        fields = ['user', 'total_value']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'