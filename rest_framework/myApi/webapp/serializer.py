from rest_framework import serializer
#from rest_framework import Employees


class EmployeesSerializer(serializer.ModelSerializer):

    class Meta:
        models=Employees
        fields=('first_name','last_name','id_number','phone_number')

    fields='__all__'
