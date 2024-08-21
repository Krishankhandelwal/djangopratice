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
            print(serializer.instance.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
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




# from django.http import JsonResponse
# from django.views import View
# import requests
# import urllib.parse

# GOOGLE_API_KEY = 'your_google_api_key_here'  # Replace with your actual Google API key

# class MapView(View):
#     def get(self, request):
#         startpoint = request.GET.get('startpoint')
#         endpoint = request.GET.get('endpoint')
#         midpoints = request.GET.getlist('midpoints')

#         if not startpoint or not endpoint:
#             return JsonResponse({'error': 'startpoint and endpoint are required'}, status=400)

#         # Split the midpoints by comma if passed as a single string
#         if len(midpoints) == 1 and ',' in midpoints[0]:
#             midpoints = midpoints[0].split(',')

#         points = [startpoint] + midpoints + [endpoint]

#         # Get latitude and longitude for each point
#         locations_with_coordinates = []
#         for point in points:
#             location_info = self.get_lat_lng(point)
#             if location_info:
#                 locations_with_coordinates.append(location_info)
#             else:
#                 return JsonResponse({'error': f'Could not geocode location: {point}'}, status=400)

#         return JsonResponse({
#             'locations': locations_with_coordinates,
#             'map_url': self.generate_map_url(points)
#         })

#     def get_lat_lng(self, location):
#         """Get latitude and longitude for a given location using Google Geocoding API."""
#         endpoint = f"https://maps.googleapis.com/maps/api/geocode/json"
#         params = {
#             'address': location,
#             'key': GOOGLE_API_KEY
#         }
#         response = requests.get(endpoint, params=params)
#         if response.status_code == 200:
#             data = response.json()
#             if data['status'] == 'OK':
#                 location_data = data['results'][0]['geometry']['location']
#                 return {
#                     'name': location,
#                     'latitude': location_data['lat'],
#                     'longitude': location_data['lng']
#                 }
#         return None

#     def generate_map_url(self, points):
#         base_url = "https://www.google.com/maps/dir/"
#         # URL encode each point to ensure proper formatting in the URL
#         encoded_points = [urllib.parse.quote(point.strip()) for point in points]
#         url = base_url + "/".join(encoded_points)
#         return url





from django.http import JsonResponse
from django.views import View
import requests
import urllib.parse

class MapView(View):
    def get(self, request):
        startpoint = request.GET.get('startpoint')
        endpoint = request.GET.get('endpoint')
        midpoints = request.GET.getlist('midpoints')

        if not startpoint or not endpoint:
            return JsonResponse({'error': 'startpoint and endpoint are required'}, status=400)

        # Split the midpoints by comma if passed as a single string
        if len(midpoints) == 1 and ',' in midpoints[0]:
            midpoints = midpoints[0].split(',')

        points = [startpoint] + midpoints + [endpoint]

        # Get latitude and longitude for each point using Nominatim
        locations_with_coordinates = []
        for point in points:
            location_info = self.get_lat_lng(point)
            if location_info:
                locations_with_coordinates.append(location_info)
            else:
                return JsonResponse({'error': f'Could not geocode location: {point}'}, status=400)

        return JsonResponse({
            'locations': locations_with_coordinates,
            'map_url': self.generate_map_url(points)
        })

    def get_lat_lng(self, location):
        """Get latitude and longitude for a given location using Nominatim API."""
        endpoint = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': location,
            'format': 'json',
            'limit': 1
        }
        try:
            response = requests.get(endpoint, params=params, timeout=10)  # Set a timeout
            if response.status_code == 200:
                data = response.json()
                if data:
                    location_data = data[0]
                    return {
                        'name': location,
                        'latitude': location_data['lat'],
                        'longitude': location_data['lon']
                    }
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        return None


    def generate_map_url(self, points):
        base_url = "https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&route="
        # URL encode each point to ensure proper formatting in the URL
        encoded_points = ["{}%2C{}".format(urllib.parse.quote_plus(point.strip()), "node") for point in points]
        url = base_url + "/".join(encoded_points)
        return url

