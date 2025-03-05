from django.shortcuts import redirect, render
from .models import Employee

def dashboard(request):
    employees = Employee.objects.all()
    return render(request, 'employees/dashboard.html', {'employees': employees})

def employee_form(request):
    return render(request, 'employees/form.html')

def submit_employee(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        age = request.POST.get("age")
        address = request.POST.get("address")
        employee_id = request.POST.get("employee_id")

        # Save data to the database
        Employee.objects.create(
            name=name,
            number=number,
            age=age,
            address=address,
            employee_id=employee_id
        )

        # Redirect to the dashboard
        return redirect('dashboard')

def dashboard(request):
    employees = Employee.objects.all()  # Retrieve all employee records
    return render(request, 'employees/dashboard.html', {'employees': employees})