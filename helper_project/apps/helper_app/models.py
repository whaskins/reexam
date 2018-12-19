from django.db import models

# Create your models here.
from apps.login_app.models import User
class JobManager(models.Manager):
    def validateJob(self, data):
        errors = {}
        print(data.get('name'))
        if len(data.get('name')) < 3:
            errors['name'] = "Job name must be at least 3 characters"
        if len(data.get('location')) < 3:
            errors['location'] = "Job location must be at least 3 characters"
        if len(data.get('desc')) < 3:
            errors['desc'] = "Job desc must be at least 3 characters"
        return errors
class Job(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='posted_jobs')
    grabbed_by = models.ManyToManyField(User, related_name='doing_jobs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.CharField(max_length=255, default=True)
    objects = JobManager()

# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     jobs_in_category = models.ManyToManyField(Job, related_name='categories', blank=True, null=True)
