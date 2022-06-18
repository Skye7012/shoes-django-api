from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shoes.viewSets import *

router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)
router.register(r'season', SeasonViewSet)
router.register(r'destination', DestinationViewSet)
router.register(r'shoe', ShoeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
