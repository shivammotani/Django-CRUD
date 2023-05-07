from rest_framework import serializers
from .models import Employee,Positions

class PositionsSerializer(serializers.ModelSerializer):
    title =  serializers.CharField(label="Position ID")
    class Meta:
        model = Positions
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionsSerializer()
    class Meta:
        model = Employee
        fields = ['id', 'fullname', 'emp_code', 'mobile', 'position']

    def create(self, validated_data):
        position_data = validated_data.pop('position')
        pos = position_data['title']
        name = validated_data['fullname']
        emp_code = validated_data['emp_code']
        mobile = validated_data['mobile']
        employee = Employee.objects.create(fullname=name, emp_code=emp_code, mobile=mobile, position_id=pos)
        return employee
    
    def update(self, instance, validated_data):
        position_data = validated_data.pop('position', None)
        validated_data['position_id'] = position_data['title']
        return super().update(instance, validated_data)
    
    


