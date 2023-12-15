from django.db import models



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
    CPU = models.CharField(max_length=255,null=True)
    GPU = models.CharField(max_length=255,null=True)
    PublicDate = models.DateField(null=True)
    Ram = models.IntegerField(null=True)
    RamType = models.IntegerField(null=True)
    Size = models.FloatField(null=True)
    Price = models.IntegerField(null=True)
    
# Create your models here.
