from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, LandLordViewSet, TenantViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'landlords', LandLordViewSet)
router.register(r'tenants', TenantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
