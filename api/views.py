from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view  
from django.db.models import Q
from .models import *
from .serializers import *
# from rest_framework.filters import SearchFilter

# Create your views here.
@api_view(["GET","POST"])
def companies(request):
    data = Company.objects.all()

    if request.method == "GET":
        data_serializer = CompanySerializer(data, many = True)
    
        return Response({
            "message": "DATA Fetch Successfully",
            "data": data_serializer.data
        })
    elif request.method == "POST":
        data_serializer = CompanySerializer(data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                "message":"Data Saved Successfully",
                "data": data_serializer.data
            })

@api_view(["GET","DELETE","PUT","PATCH"])
def companies_data(request,id):
        data = Company.objects.get(id=id)
        # instance = get_object_or_404(Company, id=id)
        if request.method == "DELETE":
            data.delete()
            return Response({
                "message":"Data Delete Successfully",
            })
        
        elif request.method == "GET":
            data_serializer = CompanySerializer(data)
            return Response({
                "message":f"{data} get Successfuly",
                "data": data_serializer.data
            })
        
        elif request.method == "PUT":
            data_serializer = CompanySerializer(data , data=request.data)
            if data_serializer.is_valid():
                data_serializer.save()
                return Response({
                    "message":"Data Update Successfully",
                    "data" : data_serializer.data
            })

        else:
            data_serializer = CompanySerializer(data, data=request.data ,partial=True)
            if data_serializer.is_valid():
                data_serializer.save()
                return Response({
                    "message":"Update Successfull",
                    "data": data_serializer.data
                })

        return Response({
            "message":"Not valid Function"
        })

@api_view(['GET'])
def search(request):
    query = request.query_params.get('search',None)
    if query:
        val= Company.objects.filter(
            Q(name__icontains =query) |
            Q(location__icontains =query) |
            Q(about__icontains =query) |
            Q(company_type__icontains =query) 
        )
        data_serializer = CompanySerializer(val,many=True)
        return Response({
                "message":f"Data get Successfully",
                "data": data_serializer.data
            })
    