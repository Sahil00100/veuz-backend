from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    custom_values = models.JSONField() 

    """
    {data:[
    {"id":12,"field_name":"age","data_type":"Int","value":24,"label":"Your age"},
    ]}
    """


class CustomField(models.Model):
    label = models.CharField(max_length=100)
    field_name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=50)  




