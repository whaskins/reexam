from django.shortcuts import render, redirect
from apps.helper_app.models import *
from django.contrib import messages

# Create your views here.
def dashboard(request):
    if 'uid' not in request.session:
        return redirect('/')
    print(request.session['uid'])
    data = {
        'userJobs': Job.objects.filter(grabbed_by=User.objects.get(id=request.session['uid'])),
        'jobs': Job.objects.exclude(grabbed_by=User.objects.get(id=request.session['uid'])),
        'first_name': User.objects.get(id=request.session['uid']).first_name,
    }
    return render(request, 'helper_app/dashboard.html', data)
    
def new(request):
    if 'uid' not in request.session:
        return redirect('/')
    return render(request, 'helper_app/new.html')
    
    
def create(request):
    print('*'*1000)
    errors = Job.objects.validateJob(request.POST)
    if len(errors) > 0:
        for key, error in errors.items():
            messages.error(request, error, extra_tags=key)
        return redirect('/jobs/new')
    newJob = Job.objects.create(name = request.POST.get('name'), location = request.POST.get('location'), desc = request.POST.get('desc'), created_by = User.objects.get(id=request.session['uid']))
    # newJob.save()
    print('categories',request.POST.get('categories'))
    catString = ""
    for cat in ['Cleaning', 'Cooking', 'Decorating', 'Other']:
        catString += request.POST.get(cat) + ', '
    try:
        catString = catString[:-2]
    except:
        pass
    newJob.categories = catString
    newJob.save()
    newJob.save()
    return redirect('/dashboard')
def addJob(request, job_id):
    thisjob = Job.objects.get(id=job_id)
    print(thisjob)
    thisjob.grabbed_by.add(User.objects.get(id=request.session['uid']))
    thisjob.save()
    return redirect('/dashboard')
def show(request, job_id):
    data = {
        'job': Job.objects.get(id=job_id),
        'first_name': User.objects.get(id=request.session['uid']).first_name,

    }
    print(Job.objects.get(id=job_id).categories)
    return render(request, "helper_app/show.html", data)
def delete(request, job_id):
    thisjob = Job.objects.get(id=job_id)
    thisjob.delete()
    return redirect('/dashboard')
def edit(request, job_id):
    data = {
    'job': Job.objects.get(id=job_id),
    'first_name': User.objects.get(id=request.session['uid']).first_name,
    }
    return render(request, 'helper_app/edit.html', data)
def giveUp(request, job_id):
    thisjob = Job.objects.get(id=job_id)
    thisjob.grabbed_by.remove(User.objects.get(id=request.session['uid']))
    thisjob.save()
    return redirect('/dashboard')
def update(request, job_id):
    errors = Job.objects.validateJob(request.POST)
    if len(errors) > 0:
        for key, error in errors.items():
            messages.error(request, error, extra_tags=key)
        return redirect('/jobs/%s/edit' % job_id)
    thisjob = Job.objects.get(id=job_id)
    thisjob.name = request.POST.get('name')
    thisjob.desc = request.POST.get('desc')
    thisjob.location = request.POST.get('location')
    thisjob.name = request.POST.get('name')
    catString = ""
    for cat in ['Cleaning', 'Cooking', 'Decorating', 'Other']:
        if request.POST.get(cat):
            catString += request.POST.get(cat) + ', '
    try:
        catString = catString[:-2]
    except:
        pass
    thisjob.categories = catString
    thisjob.save()
    # for cat in ['Cleaning', 'Cooking', 'Decorating', 'Other']:
    #     if request.POST.get('other'):
    #         Category.objects.create(name = request.POST.get('other'))
    #     catObj = Category.objects.get(name=request.POST.get(cat))
    #     thisjob.categories.add(catObj)
    return redirect('/dashboard')

