from django.shortcuts import render,redirect
from .models import Department,Employee

# Create your views here.

def home(request):
    employe = Employee.objects.all()
    context = { 'employee':employe}
    return render(request, 'index.html', context) 

def addnew(request):
    department=Department.objects.all()
    context={'department':department}
    if request.method=='POST':
      empId = request.POST.get('empId')
      empNamae = request.POST.get('empName')
      department=Department.objects.get(name=request.POST['dept'])
      
      #aa=routine(course=co,date=dat,start=start,end=end)

      user=Employee()
      user.Emp_id  = empId
      user.Emp_name=empNamae
      user.emp_dep =department
      user.save()
        
        
    return render(request,'addnew.html',context)


def delete(request,id):
  
    obj =Employee.objects.filter(Emp_id=id)
    obj.delete();    
    return redirect('home')

def updaterecord(request,id):
  
      empId = request.POST.get('empId')
      empNamae = request.POST.get('empName')
      department=Department.objects.get(name=request.POST['dept'])
      
      #aa=routine(course=co,date=dat,start=start,end=end)

      user=Employee()
      user.Emp_id  = empId
      user.Emp_name=empNamae
      user.emp_dep =department
      user.save()
      return redirect('home')
  
  
def update(request,id):
    employe=Employee.objects.get(Emp_id=id)
    context={'employe':employe}
    return render(request,'update.html',context)