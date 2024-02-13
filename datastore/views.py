from django.http import HttpResponse
from django.shortcuts import render
from store.models import Employee


def index(request):
    if request.method=="POST":
        f_name = request.POST["fname"]
        l_name = request.POST["lname"]
        email = request.POST["email"]
        date = request.POST["dob"]
        state = request.POST["state"] 

        employee = Employee(F_name = f_name,l_name = l_name, email=email,date=date,state=state )
        employee.save()

    return render(request, 'index.html')