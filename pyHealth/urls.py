from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('employee_data', views.employee_data, name="employee_data"),
]