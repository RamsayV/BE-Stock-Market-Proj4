
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main_app import views
from main_app.views import MyTokenObtainPairView



from rest_framework_simplejwt.views import (
   TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'users', views.UserViewset)
router.register(r'groups', views.GroupViewset)
router.register(r'portfolios', views.PortfolioViewSet)
router.register(r'portfoliosadd', views.PortfolioAddViewSet, basename="addportfolio")
router.register(r'portfoliodelete', views.PortfolioDeleteViewSet, basename="deleteportfolio")
router.register(r'portfolioupdate', views.PortfolioUpdateViewSet, basename="updateportfolio")
router.register(r'stockportfolios', views.StockPortfolioViewSet)
router.register(r'addstockportfolios', views.StockPortfolioAddViewSet, basename="addstockportfolios")
router.register(r'stocks', views.StockViewSet)
router.register(r'stocksadd', views.StockAddViewSet, basename="addstock")
router.register(r'stocksdelete', views.StockDeleteViewSet, basename="deletestock")
router.register(r'stocksupdate', views.StockUpdateViewSet, basename="updatestock")
router.register(r'transactions', views.TransactionViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', views.CreateUser.as_view(), name ='signup'),
]
