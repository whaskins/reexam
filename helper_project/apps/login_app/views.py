from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    request.session['reg_info'] = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'email': 'Email',
        'password': 'Password',
        'confpword': 'Confirm Password'
    }
    request.session['login_info'] = {
        'email': 'Email',
        'password': 'Password'
    }
    return render(request, 'login_app/index.html')
def register(request):
    errors = User.objects.validate(request.POST)
    if len(errors) > 1:
        for t, error in errors.items():
            messages.error(request, error, extra_tags=[t, 'reg'])
        print(type(messages.error))
        return redirect('/')
    user = User.objects.create(
        first_name = request.POST.get('first_name'),
        last_name = request.POST.get('last_name'),
        email = request.POST.get('email'),
        password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())

    )
    request.session['uid'] = user.id

    
    return redirect('/success')
    
def login(request):
    errors = User.objects.validateEmail(request.POST)
    if len(errors) > 1:
        for t, error in errors.items():
            messages.error(request, error, extra_tags=[t, 'login'])
        print(type(messages.error))
        return redirect('/')
    user = User.objects.get(email=request.POST.get('email'))
    if bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
        request.session['uid'] = user.id
        return redirect('/success')
    else:
        return HttpResponse('fail')

def logout(request):
    request.session['uid'] = None
    return redirect('/')
def success(request):
    if request.session['uid'] is None:
        return redirect('/')
    user = User.objects.get(id=request.session['uid'])
    data = {
        'name': user.first_name
    }
    return redirect('/dashboard')

def show(request, job_id):
    data = {
        job: Job.objects.get(id=job_id)
    }