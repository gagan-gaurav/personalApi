from django.urls import include, path

from rest_framework import routers

from .views import PortfolioViewSet

router = routers.DefaultRouter()
router.register(r'portfolio', PortfolioViewSet)
# router.register(r'species', SpeciesViewSet)

urlpatterns = [
   path('', include(router.urls)),
]