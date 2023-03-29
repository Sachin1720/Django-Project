from django.shortcuts import render, HttpResponse, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


def home(request):
    return render(request, 'welcome.html')


def loadform(request):
    form = EmployeeForm
    return render(request, 'loadform.html', {'form': form})


def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('showall')


def showall(request):
    emp = Employee.objects.all()
    return render(request, 'showall.html', {'emp': emp})


def edit(request, id):
    emp = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'emp': emp})


def update(request, id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=emp)
    form.save()
    return redirect('showall')


def delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('showall')


def search(request):
    search = request.POST.get('search')
    emp = Employee.objects.filter(firstname__icontains=search)

    return render(request, 'showall.html', {'emp': emp})
