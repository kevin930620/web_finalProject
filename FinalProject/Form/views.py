from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib import auth
from django.shortcuts import render

from Form.form import LoginForm

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
                
                main_html = loader.get_template('main.html')
                context = {'user': request.user,
                           'messages':'login ok'}
                return HttpResponse(main_html.render(context,request))
            else:
                
                print('Login failed')
                context = {
                    'title':'Login Fail',
                    'post_form':post_form,
                }
                return HttpResponse(template.render(context,request))
        else:
            print('Login ERROR')
            return HttpResponse(template.render())
    else:
        print('ERROR')
    
def logout(request):
    auth.logout(request)
    main_html = loader.get_template('main.html')
    context={'user': request.user}
    return HttpResponse(main_html.render(context,request))


# Create your views here.
