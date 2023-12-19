from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib import auth

from Form.form import LoginForm

def login(request):
    template = loader.get_template('login.html')
    messages = ''
    if request.method == "POST":
        post_form = LoginForm(request.POST)
        if post_form.is_valid():
            username = post_form.changed_data['username']
            password = post_form.changed_data['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                auth.login(request,user)
                messages = f'{username} Login'
                main_html = loader.get_template('main.html')
                context = {'user': request.user}
                return HttpResponse(main_html.render(context,request))
            else:
                messages = 'Login failed'
            print(messages)
    else:
        post_form = LoginForm()
    context = {
        'user' : request.user,
        'post_form': post_form,
        'message' : messages,
    }
    return HttpResponse(template.render(context,request))

def logout(request):
    auth.logout(request)
    main_html = loader.get_template('main.html')
    context={'user': request.user}
    return HttpResponse(main_html.render(context,request))


# Create your views here.
