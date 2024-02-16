from django.urls import path

from app import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('services', views.Service.as_view(), name='services'),
    path('method', views.Method.as_view(), name='method'),
    path('about', views.About.as_view(), name='about'),
    path('job-vacancies', views.Job.as_view(), name='job-vacancies'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('job-application', views.JobApplication.as_view(), name='job-application'),
    path('project-planner', views.ProjectPlanner.as_view(), name='project-planner'),
]