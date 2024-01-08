from django.contrib import admin
from .models import Computer,Test,BrandType,GPUBrands,GPUType,CPUType,wishlist

class ComputerAdmin(admin.ModelAdmin):
    list_display = ("ComputerName","Brand")

# class TestAdmin(admin.ModelAdmin):
#     list_display=("name","parent")


admin.site.register(Computer,ComputerAdmin)
admin.site.register(Test)
admin.site.register(BrandType)
admin.site.register(GPUType)
admin.site.register(GPUBrands)
admin.site.register(CPUType)
admin.site.register(wishlist)

# Register your models here.
