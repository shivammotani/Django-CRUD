from employee_register.viewsets import EmployeeViewSet,PositionsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewSet)
router.register(r'positions', PositionsView, basename='positions')
