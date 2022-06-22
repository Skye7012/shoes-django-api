from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shoes.Routers.UserRouter import UserRouter
from shoes.viewSets import *

router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)
router.register(r'season', SeasonViewSet)
router.register(r'destination', DestinationViewSet)
router.register(r'shoe', ShoeViewSet)
router.register(r'size', SizeViewSet)
router.register(r'order', OrderViewSet, basename='order')

user_router = UserRouter()
user_router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(user_router.urls)),
]
