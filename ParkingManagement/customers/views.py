from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Customer
from .serializers import CustomersSerializer

class Customerslist(APIView):
    def get(self, request):
        CustomersList = Customer.objects.all()
        serializer = CustomersSerializer(CustomersList, many=True) #converts everying to json
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
