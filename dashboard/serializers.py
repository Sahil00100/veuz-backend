
from dashboard.models import CustomField,Employee
from rest_framework import serializers


class CustomFieldSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    class Meta:
        model = CustomField
        fields = "__all__"

    def get_value(self,ins):
        return ""



class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Employee
        fields = "__all__"