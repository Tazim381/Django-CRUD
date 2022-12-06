from django.db import models

# Create your models here.


class Department(models.Model):
    name=models.CharField( max_length=50)
    def __str__(self):
     return f'{self.name}'
    
    
class Employee(models.Model):
    Emp_id = models.CharField(unique=True,primary_key=True,max_length=255)
    Emp_name=models.CharField(max_length=255)
    emp_dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
     return f'{self.Emp_name}'
 
 
    
    
    