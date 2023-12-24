from django.db import models

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Data(models.Model):
    name=models.CharField(max_length=300)
    dob=models.TextField(default=True)
    age=models.IntegerField(default=True)
    gender=models.TextField(default=True)
    phone=models.IntegerField(default=True)
    mail=models.EmailField(default=True)
    address=models.TextField(default=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE,default=True)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,default=True)
    account=models.TextField(default=True)
    material=models.TextField(default=True)

    def __str__(self):
        return self.name