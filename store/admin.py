from django.contrib import admin
from store.models import Employee

# Register your models here.

class Employeeadmin(admin.ModelAdmin):
    list_display = ('F_name', 'l_name','email','date','state')

admin.site.register(Employee, Employeeadmin)

