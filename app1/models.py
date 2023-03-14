from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    marks = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta():
        db_table = 'student'





# cmd----django-admin startproject b8_REST-------------------------------------
# then--pip install djangorestframework pip install djangorestframework---------------------------

#---setting installed app----'rest_framework'
# -python manage.py startapp app1
# django mysql database seeting---------------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'DB_NAME', name
#         'USER': 'DB_USER',  root
#         'PASSWORD': 'DB_PASSWORD', golu
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }
# # 
# class Student(models.Model):--------------------------------
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     address = models.CharField(max_length=100)
#     marks = models.IntegerField()
    
#     def __str__(self):
#         return self.name
    
#     class Meta():
#         db_table = 'student'

#admin------------------------------------
# from django.contrib import admin
# from .models import Student
# # Register your models here.
# admin.site.register([Student])


# 01 makemigrations - migrate -]
#  serialization----->complex data ko convert karta hai python dict-----pyton dict milne par NSL json
 
#  deserialization====> Complex Depr
 
 
#  [JsonRender-python dict to Json
#  json{arser ---Json to python dict}          NSL = network support language

# we are working for producer---to Develop Api]

# 02..py manage.py createsuperuser
#..3 runserver
# (djangorestframework)
# serailizer  serializer


# 04..mdels me aap1 me ek file create serializers.py 
# from rest_framework import serializers

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 100)
#     age = serializers.IntegerField()
#     address = serializers.CharField(max_length=100)
#     marks = serializers.IntegerField()


# 05..views
# rom django.shortcuts import render

# # Create your views here.
# from .models import Student
# from serializers import StudentSerializer
# from django.http import HttpResponse

# def get_student(request, id):  #single student student
#   print(id)
#     return HttpResponse("Success")


# 06...
# rom django.contrib import admin
# from django.urls import path
# from app1 import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/get-student/<intLid>/',view.get_student),
# ]
# 07..# py manage/py runserver
# gogle par runserver copy http://127.0.0.1:8000/api/get-student/1/

# #run 1
# [09/Feb/2023 15:43:38] "GET /api/get-student/1/ HTTP/1.1" 200 7

# 08..d drive me jo B8_REST foler me

# app1
# B8_REST
# manage.py --manage.py file ke niche ek textfile create karna hai
# API_Endpoints.txt isme id pass 
# http://127.0.0.1:8000/api/get-student/1/ --- id -- student --
