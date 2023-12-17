from rest_framework import viewsets
from .models import Pack
from .serializers import PackSerializer

class PackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer