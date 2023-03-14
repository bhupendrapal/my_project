import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
import json
from django.views.decorators.csrf import csrf_exempt


# def get_student(request, id):  #single student student
    #print(id) #http://127.0.0.1:8000/api/get-student/1/
    # stud_obj = Student.objects.get(id=id)
    # print(stud_obj.__dict__)  #01......http://127.0.0.1:8000/api/get-student/1/
    #'#'stud ki dictionery=={'_state': <django.db.models.base.ModelState object at 0x000001CAD28F0CA0>, 'id': 1, 'name': 'Lokesh', 'age': 25, 'address': 'Borgaon', 'marks': 85}
# [09/Feb/2023 15:53:12] "GET /api/get-student/1/ HTTP/1.1" 200 7
# {'_state': <django.db.models.base.ModelState object at 0x000001CAD28F06D0>, 'id': 1, 'name': 'Lokesh', 'age': 25, 'address': 'Borgaon', 'marks': 85}
# [09/Feb/2023 15:53:23] "GET /api/get-student/1/ HTTP/1.1" 200 7'''

    # stud_obj.__dict__.pop("_state") #02..............................
    # print(stud_obj.__dict__)
    # return HttpResponse("Success")
    
#     '''{'id': 1, 'name': 'Lokesh', 'age': 25, 'address': 'Borgaon', 'marks': 85}
# [09/Feb/2023 16:08:51] "GET /api/get-student/1/ HTTP/1.1" 200 7''''

#(after import json)03.....................................
    # stud_obj = Student.objects.get(id=id)  #03...............................
    # stud_obj.__dict__.pop("_state")
    # data = json.dumps(stud_obj.__dict__)
    # print(data)
    # return HttpResponse("Success")
#   Run''''{"id": 1, "name": "Lokesh", "age": 25, "address": "Borgaon", "marks": 85}
    #  [09/Feb/2023 16:38:10] "GET /api/get-student/1/ HTTP/1.1" 200 7'''------{"id": 1, "name": "Lokesh", "age": 25, "address": "Borgaon", "marks": 85}  or seond id http://127.0.0.1:8000/api/get-student/2/


    # stud_obj = Student.objects.get(id=id)  #03...............................
    # stud_obj.__dict__.pop("_state")
    # data = json.dumps(stud_obj.__dict__)
    # return HttpResponse(data)
#'''{"id": 1, "name": "Lokesh", "age": 25, "address": "Borgaon", "marks": 85}''' #from google{"id": 1, "name": "Lokesh", "age": 25, "address": "Borgaon", "marks": 85}

# postman se bhi GET request
#using serializer  and uncomment import json

# def get_student(request, id):
#     stud_obj = Student.objects.get(id=id) #COMPLEX DATA #04...............................
#     python_data =StudentSerializer(stud_obj) #python dictionery
#     print(python_data.data)
#     return HttpResponse("Success")

#{'name': 'Lokesh', 'age': 25, 'address': 'Borgaon', 'marks': 85}

# def get_student(request, id):
#     stud_obj = Student.objects.get(id=id) #COMPLEX DATA #04...............................
#     python_data =StudentSerializer(stud_obj) #python dictionery
#     json_data = JSONRenderer().render(python_data.data)
#     print(type(json_data))
#     return HttpResponse("Success")


def get_student(request, id):
    stud_obj = Student.objects.get(id=id) #COMPLEX DATA #04...............................
    python_data =StudentSerializer(stud_obj) #python dictionery
    bytes_data = JSONRenderer().render(python_data.data) #json.dumps
    return HttpResponse(bytes_data, content_type = "application/json")

#{"name":"Lokesh","age":25,"address":"Borgaon","marks":85,"is_active":true}
# id	1
# name	"Lokesh"
# age	25
# address	"Borgaon"
# marks	85
# is_active	true
# 1	
# id	2
# name	"Sunil"
# age	23
# address	"Sausar"
# marks	78
# is_active	true
# 2	
# id	3
# name	"golu"
# age	29
# address	"Nagpu"
# marks	89
# is_active	true
# 3	
# id	4
# name	"atul"
# age	26
# address	"mumbai"
# marks	88
# is_active	true

def get_all_students(request):
    all_studs = Student.objects.all()
    python_data = StudentSerializer(all_studs,many=True)
    bytes_data = JSONRenderer().render(python_data.data)
    return HttpResponse(bytes_data, content_type = "application/json")

# def create_student(request):
#     if request.method == "POST":              #import json
        
#         pass
#     else:
#         error_msg = {"msg":"Only post method is allowed."}
#         json_data = json.dumps(error_msg)
#         return HttpResponse(json_data, content_type = "application/json",status=status.HTTP_405_METHOD_NOT_ALLOWED)
        #{"msg": "Only post method is allowed."}
        
@csrf_exempt     
def create_student(request):
    if request.method == "POST":              #import json (request.body se bytes )
        # print(request.body)  # request data body data milega postman me post request and name: Age: marks: address}
        # print(dir(request))  
        # print(request.data) #user
        print(request.build_absolute_uri)
        return HttpResponse("POST request",status=status.HTTP_201_CREATED)
        
    else:
        error_msg = {"msg":"Only post method is allowed."}
        json_data = json.dumps(error_msg)
        return HttpResponse(json_data, content_type = "application/json",status=status.HTTP_405_METHOD_NOT_ALLOWED)   #postman nody raw json