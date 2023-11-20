from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions,status
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer,PortfolioSerializer,StockSerializer, StockPortfolioSerializer,TransactionSerializer
from .models import Portfolio, Stock, Transaction, StockPortfolio
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions, generics

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        
        token['username'] = user.username
        

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class =  UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserSerializer


class GroupViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class =  GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

class StockViewSet(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Stock.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Stock.objects.filter(portfolios__user=user)


class StockPortfolioViewSet(viewsets.ModelViewSet):
    queryset = StockPortfolio.objects.all()
    serializer_class = StockPortfolioSerializer

class StockAddViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class StockDeleteViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class StockUpdateViewSet(viewsets.ModelViewSet):
    queryset =Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()