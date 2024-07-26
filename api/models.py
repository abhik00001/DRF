from django.db import models

# Create your models here.

#company model
class Company(models.Model):
    name =  models.CharField(max_length=80)
    location = models.CharField( max_length=150)
    about = models.TextField()
    company_type = models.CharField( max_length=100,choices=(('IT','IT'),('Non IT', 'NOn IT'),('Mobile Phones','Mobile Phones')) )

    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# class Employee(models.Model):
#     company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     about = models.TextField()
#     skills = models.CharField(max_length=150)
#     added_date = models.DateTimeField(auto_now=True)
