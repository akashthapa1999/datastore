from django.db import models

# Create your models here.

class Employee(models.Model):
    F_name = models.CharField("fname", max_length=50)
    l_name = models.CharField("lname", max_length=50)
    email = models.EmailField("email", max_length=254)
    date = models.DateField("dob", auto_now=False, auto_now_add=False)
    state = models.CharField("state", max_length=50) 

    
    
