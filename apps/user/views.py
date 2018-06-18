import re
from django.shortcuts import render, redirect
from django.contrib import messages
from . import models as m

# Create your views here.

EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$')

def is_blank(request, name, field):
    if len(field) == 0:
        messages.error(request, '{} cant be blank'.format(name))
        return True
    return False

def index(request):
    if request.method == 'POST':
        try:
            user = m.User.objects.get(email=request.POST['html_email'])
            if user.password == request.POST['html_password']:
                request.session['user_id'] = user.id
                request.session['name'] = user.name            
                # setup_web_session(user)
                return render(request, 'user/index.html')
            else:
                messages.error(request, 'password didn\'t macth')    
        except:
            messages.error(request, 'invalid login')

    return render(request, 'user/index.html')

def register(request):
    if request.method == 'POST':

        is_valid = False
        name = request.POST['html_name']
        email = request.POST['html_email']
        password = request.POST['html_password']
        confirm = request.POST['html_confirm']

        is_valid = not is_blank(request, 'name', name)
        is_valid = not is_blank(request, 'email', email)
        is_valid = not is_blank(request, 'password', password)
        is_valid = not is_blank(request, 'confirm', confirm)

        if not EMAIL_REGEX.match(email):
            is_valid = False
            messages.error(request, 'invalid email format')

        if password != confirm:
            is_valid = False
            messages.error(request, 'password did not match')
        
        if(len(password) < 6):
            is_valid = False
            messages.error(request, 'password is too short')    

        if is_valid:
            try:
                user = m.User()
                user.name = request.POST['html_name']
                user.email = request.POST['html_email']
                user.password = request.POST['html_password']
                user.save()
                request.session['user_id'] = user.id
                request.session['name'] = user.name            
                # setup_web_session(user)
                return render(request, 'user/index.html')
            except:
                messages.error(request, 'invalid input')               

    return render(request, 'user/register.html')


def logout(request):
    request.session.clear()
    return redirect('user:index')

def setup_web_session(request, user):
    request.session['user_id'] = user.id
    request.session['username'] = user.username
    return True

