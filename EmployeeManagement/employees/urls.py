from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_form'),  # Form page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('submit/', views.submit_employee, name='submit_employee'),  # Form submission
]
