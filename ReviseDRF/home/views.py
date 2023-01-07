from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import EmployeeDataSerializer
from .models import EmployeeData
import json
# Create your views here.


@api_view()
def home(request):
    return Response({
        'name': 'Garv',
        'age': 21,
    })

# create a method to save employee data to DB


@api_view(['POST'])
def setEmployeeData(request):
    try:
        data = request.data
        serializer = EmployeeDataSerializer(
            data=data)   # deserializing data
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Data sent successfully'
            })
        else:
            return Response({
                'status': False,
                'data': serializer.errors  # serializer.errors can only be used when date is validated
            })

    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong'
        })


# create method to fetch employee data from DB

@api_view(['GET'])
def getEmployeeData(request):
    try:
        data = EmployeeData.objects.all()

        # many=True because here more than one object will come as we are fetching all
        serializer = EmployeeDataSerializer(data, many=True)
        # print(serializer.data)
        # json_data = json.dumps(serializer.data) - There is no need to use json to convert python dict to json
        return Response({
            'status': True,
            'data': serializer.data
        })
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'data': "Something went wrong"
        })
