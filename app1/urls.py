from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('student_list/',student_list ),
    path("s_list/",employee_list),
    path("emp_list/",emp_list),
    path("emp_list_id/<int:pk>/",emp_update)
]
