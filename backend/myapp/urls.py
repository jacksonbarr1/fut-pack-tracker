from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myapp.views import PackViewSet

router = DefaultRouter()
router.register(r'packs', PackViewSet)

urlpatterns = [
    path('', include(router.urls))
]