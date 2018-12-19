from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/$', views.dashboard),
    url(r'^/new$', views.new),
    url(r'^/create$', views.create),
    url(r'^/(?P<job_id>\d+)/add$', views.addJob),
    url(r'^/(?P<job_id>\d+)/delete$', views.delete),
    url(r'^/(?P<job_id>\d+)/edit$', views.edit),
    url(r'^/(?P<job_id>\d+)/update$', views.update),
    url(r'^/(?P<job_id>\d+)/give_up$', views.giveUp),
    url(r'^/(?P<job_id>\d+)$', views.show),

    
]
