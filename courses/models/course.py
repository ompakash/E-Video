from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=200, null= True)
    price = models.IntegerField(null=False,default=0)
    discount = models.IntegerField(null=False,default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='files/thumbnail')
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to='files/resource')
    lengtt = models.IntegerField(null=False)
     
