from django.db import models
from django.contrib.auth.models import User


class BrandType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class GPUBrands(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class GPUType(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(GPUBrands,on_delete=models.CASCADE,default=True)
    def __str__(self):
        return self.name

class CPUType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Test(models.Model):
    name = models.CharField(max_length=100,default=True)


class Computer(models.Model):
    ComputerName = models.CharField(max_length=255)
    Brand = models.ForeignKey(BrandType,on_delete=models.CASCADE)
    CPU = models.ForeignKey(CPUType,null=True,on_delete=models.CASCADE)
    GPUBrands = models.ForeignKey(GPUBrands,null=True,on_delete=models.CASCADE)
    PublicDate = models.DateField(null=True)
    Ram = models.IntegerField(null=True)
    Size = models.FloatField(null=True)
    Price = models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.ComputerName}{self.CPU}'

class wishlist(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    computer = models.ForeignKey(Computer,on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.username}  {self.computer.ComputerName}'

# Create your models here.
