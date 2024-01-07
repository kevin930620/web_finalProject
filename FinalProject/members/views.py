from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Computer,CPUType,wishlist
from django.contrib.auth.decorators import login_required

from .form import FilterForm

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


def filter(request):
    myComputer = Computer.objects.all().values()
    theCPUType = CPUType.objects.all().values()
    template = loader.get_template('filter.html')
    context={
        'myComputer':myComputer,
        'theCpuType':theCPUType,
    }
    return HttpResponse(template.render(context,request))


def Item_List(request):
    # 
    computer = Computer.objects.all()
    filter_form = FilterForm(request.GET or None)
    template = loader.get_template('filter.html')
    if filter_form.is_valid():
        Cpu_select = filter_form.cleaned_data.get('cputype')

        if Cpu_select:
            computer = computer.filter(cpu__in=Cpu_select)

    context  ={
        'computer':computer,
        'filter_form':filter_form
    }
    return HttpResponse(template.render(context,request))




@login_required
def wish(request):
    ''' to show my booking list '''
    wishlist_computer = wishlist.objects.filter(user=request.user)
    print (f'All bookings by {request.user}:')
    for computer in wishlist_computer:
        print (computer)
    # member = getMember(request)    
    # print ('member.firstname', member.firstname)
    context = {
            #  'member': member,
               'wish': wishlist_computer}
    return render(request, 'hope.html', context)


# def getMember(request):
#     print(request.user)
    
        