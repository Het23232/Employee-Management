from django.db import models

class Employee(models.Model):
    id = models.CharField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    age = models.IntegerField()
    address = models.TextField()
    employee_id = models.CharField(max_length=10, unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = f"{self.id:04d}"  # Formats ID as 4-digit (e.g., 0001, 0002, ...)
        super().save(*args, **kwargs)
class Employee(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    employee_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name  # This will display the employee's name in the admin panel
