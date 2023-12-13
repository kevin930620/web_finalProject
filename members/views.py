from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Computer

def members(request):
    myComputer = Computer.objects.all().values()
    template = loader.get_template('models.html')
    context = {
        'myComputer' : myComputer,
    }
    return HttpResponse(template.render(context,request))

def imformation(request,id):
    myComputer = Computer.objects.get(id=id)
    template = loader.get_template('imformation.html')
    context = {
        'myComputer':myComputer
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
