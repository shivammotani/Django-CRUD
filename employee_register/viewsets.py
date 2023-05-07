from rest_framework import viewsets
from . import models
from . import serializers


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

class PositionsView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Positions.objects.all()
    serializer_class = serializers.PositionsSerializer
