from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from .models import Computer,CPUType,wishlist,User
from django.contrib.auth.decorators import login_required


from django.contrib import auth
from django.contrib.auth import authenticate

from .form import FilterForm,LoginForm,add_wishForm

def members(request):
    myComputer = Computer.objects.all().values()
    template = loader.get_template('models.html')
    context = {
        'myComputer' : myComputer,
    }
    # print(context)
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


@login_required
def view_wishlist(request):
    
    wish = wishlist.objects.filter(user=request.user)
    print (f'All bookings by {request.user}:')
    for b in wish:
        print (b)
    member = request.user    
    
    context = {'member': member,
               'wishlist_items': wish}
    return render(request, 'wishlist.html', context)

def getMember(request):
    print (request.user)
    try:
        member = User.objects.get(user=request.user)
        print (member)
        return member
    except:
        print (f"The user {request.user} is not a member")
        return render(request, 'booking_error.html', None)

def add_to_wishlist(request):
    if request.method == 'POST':
        form = add_wishForm(request.POST)
        if form.is_valid:
           form.save() 
        
        item_name = request.POST.get('item_name')
        wishlist.objects.create(user=request.user,computer = item_name)
        return redirect('view_wishlist')
    return render(request, 'add_to_wishlist.html')




def TEST(request):
    myComputer = Computer.objects.all().values()
    template = loader.get_template('master.html')
    context={
        'myComputer':myComputer,
    }
    return HttpResponse(template.render(context,request))



def login(request):
    template = loader.get_template('login.html')
    messages = ''
    if request.method == 'GET':
        post_form = LoginForm()
        context={
            'user': request.user,
            'post_form':post_form,
        }
        
        return HttpResponse(template.render(context,request))

    elif request.method == "POST":
        post_form = LoginForm(request.POST)
        if post_form.is_valid():
            username = post_form.cleaned_data['username']
            password = post_form.cleaned_data['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                auth.login(request,user)
                
                main_html = loader.get_template('models.html')
                context = {'user': request.user,
                        #    'messages':'login ok'
                           }
                print('asd')
                return HttpResponse(main_html.render(context,request))
            else:
                
                print('Login failed')
                context = {
                    'title':'Login Fail',
                    'post_form':post_form,
                }
                print('kcxjhcv')
                return HttpResponse(template.render(context,request))
        else:
            print('Login ERROR')
            return HttpResponse(template.render())
    else:
        print('ERROR')
    
def logout(request):
    auth.logout(request)
    main_html = loader.get_template('models.html')
    context={'user': request.user}
    print('zkxjc')
    return HttpResponse(main_html.render(context,request))
    