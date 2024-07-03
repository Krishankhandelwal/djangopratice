from django.shortcuts import render
from app1.models import * 
from app1.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status

# Create your views here.
# @api_view(['GET','POST']) 
# def student_list(request): 
#     if request.method == 'GET': 
#         queryset = Student.objects.all() 
#         print(queryset)
#         serializer = StudentSerializers(queryset, many=True) 
#         print(serializer.data)
#         return Response({"status":True,"message":"data is retrive ","data":serializer.data}) 
  
#     elif request.method == 'POST': 
#         serializer = StudentSerializers(data=request.data) 
#         if serializer.is_valid(): 
#             serializer.save() 
#             return Response(serializer.data,
#                             status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors, 
#                         status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        queryset = Student.objects.all()
        serializer = StudentSerializers(queryset, many=True)
        return Response({"status": True, "message": "data is retrieved", "data": serializer.data})

    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','POST'])
def employee_list (request):
    if request.method=='GET':
        queryset=Student.objects.all()
        serializer=StudentSerializers(queryset,many=True)
        return Response({"status":"True","message":"data is retrive succesfully ","data":serializer.data})


# @api_view(['GET','PUT','PATCH','DELETE']) 
# def transformer_detail(request, pk): 
#     try: 
#         transformer = Transformer.objects.get(pk=pk) 
#     except Transformer.DoesNotExist: 
#         return Response(status=status.HTTP_404_NOT_FOUND) 
  
#     if request.method == 'GET': 
#         serializer = StudentSerializers(transformer) 
#         return Response(serializer.data) 
  
#     elif request.method == 'PUT': 
#         serializer = TransformerSerializer(transformer, data=request.data) 
  
#         if serializer.is_valid(): 
#             serializer.save() 
#             return Response(serializer.data) 
#         return Response(serializer.errors, 
#                         status=status.HTTP_400_BAD_REQUEST) 
#     elif request.method == 'PATCH': 
#         serializer = TransformerSerializer(transformer, 
#                                            data=request.data, 
#                                            partial=True) 
  
#         if serializer.is_valid(): 
#             serializer.save() 
#             return Response(serializer.data) 
#         return Response(serializer.errors, 
#                         status=status.HTTP_400_BAD_REQUEST) 
  
#     elif request.method == 'DELETE': 
#         transformer.delete() 
#         return Response(status=status.HTTP_204_NO_CONTENT) 



@api_view(['GET','POST'])
def emp_list(request):
    if request.method =='GET':
        query_set=Employee.objects.all()
        serializer=EmployeSerializers(query_set,many=True)
        return Response ({"status":True,"message":"data retrive succesfully","data":serializer.data})
    elif request.method=='POST':
        serializer=EmployeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error)
    
@api_view(['GET','PUT'])
def emp_update(request,pk):
    try:
        emp=Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=EmployeSerializers(emp)
        return Response (serializer.data)
    

# @api_view(['GET','PUT','PATCH','DELETE']) 
# def emp_update(request, pk): 
#     try: 
#         transformer = Employee.objects.get(pk=pk) 
#     except Employee.DoesNotExist: 
#         return Response({"status":True,"message":"data is not found"},status=status.HTTP_404_NOT_FOUND) 
  
#     if request.method == 'GET': 
#         serializer = EmployeSerializers(transformer) 
#         return Response(serializer.data) 






