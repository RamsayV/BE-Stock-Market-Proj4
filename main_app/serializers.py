from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Portfolio, Stock, Transaction, StockPortfolio
import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username','email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'username']

class PortfolioSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Portfolio
        fields = ['user_id', 'portfolio_name', 'total_value','id']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        print(user)
        portfolio = Portfolio.objects.create(user=user, **validated_data)
        return portfolio

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class StockPortfolioSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = StockPortfolio
        fields = ['stock', 'user_id', 'portfolio', 'quantity']


    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        print(user)
        stockPortfolio = StockPortfolio.objects.create(user=user, **validated_data)
        return  stockPortfolio

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class UserSerializer (serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.pop('password')
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'detail':'Password and Confirmation do not match'})

        try:
            validation.validate_password(password=password)
        except ValidationError as err:
            raise ValidationError({'password': err})

        attrs['password'] = make_password(password)

        return attrs
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'password_confirmation']