from django.shortcuts import render
from dashboard.models import CustomField, Employee
from dashboard.serializers import CustomFieldSerializer, EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == 'GET':

        data = ["sahil"]
        return Response({"data":data})



@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def employee_settings(request):
    data = request.data
    if request.method == "GET":
        instances = CustomField.objects.filter()
        serialized_data = CustomFieldSerializer(instances,many=True).data

        response_data = {"data":serialized_data}



    elif request.method == "POST":

        required_fields = ["field_name","data_type"]
        fields_missing = [item for item in required_fields if item not in data]
        if fields_missing:
            return Response({"message":f"Required fields missing : {fields_missing}"},status=status.HTTP_400_BAD_REQUEST)


        # label = data["label"]
        field_name = data["field_name"]
        data_type = data["data_type"]

        label = field_name
        field_name = field_name.replace(" ","")


        CustomField.objects.create(
            label=label,
            field_name=field_name,
            data_type=data_type,
        )
        response_data = {"message":"Created Successfully"}


    return Response(response_data) 


import re
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def employee_view(request):
    if request.method == 'GET':
        page_number = request.GET.get("page",1)
        search = request.GET.get("search",None)
        EmployeeInstances = Employee.objects.filter()
        total_count = EmployeeInstances.count()

        if search is not None:
            EmployeeInstances  = EmployeeInstances.filter(Q(name__istartswith=search) | Q (email__startswith=search)  | Q (phone_number__startswith=search) )

        #pagination
        paginator = Paginator(EmployeeInstances, 10)
        paginated_data = paginator.get_page(page_number)

        # data = EmployeeSerializer(EmployeeInstances,many=True)
        data = []

        custom_field_instances = CustomField.objects.all()
        for item in paginated_data:
            item_data = {
                "name":item.name,
                "phone_number":item.phone_number,
                "email":item.email,
            }
            custom_values=item.custom_values or []
            for custom_item in custom_field_instances:
                custom_value_item = next((i for i in custom_values if i['id'] == custom_item.id),None)

                if custom_value_item is None:
                    item_data[custom_item.label] = ""
                else:
                    item_data[custom_item.label] = str(custom_value_item["value"]
)
            data.append(item_data)

        response_data = {"data":data,"total_count":total_count}


    elif request.method == "POST":
        data = request.data
        

        required_fields = ["name","phone_number","email"]
        fields_missing = [item for item in required_fields if item not in data]
        if fields_missing:
            return Response({"message":f"Required fields missing : {fields_missing}"},status=status.HTTP_400_BAD_REQUEST)


        name = data["name"]
        phone_number = data["phone_number"]
        email = data["email"]


        # Validate email 
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return Response({"message": "Invalid email "},status=status.HTTP_400_BAD_REQUEST)

        # Validate phone number 
        if not re.match(r"^\d{10}$", phone_number):  
            return Response({"message": "Phone number must be 10 digits."},status=status.HTTP_400_BAD_REQUEST)



        custom_values = data["custom_values"]

        Employee.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            custom_values=custom_values
        )
        response_data = {"message":"Created Successfully"}




    return Response(response_data) 






