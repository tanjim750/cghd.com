from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')


class Service(View):
    def get(self, request, *args, **kwargs):
        return render(request,'service.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request,'about.html')
    

class Method(View):
    def get(self, request, *args, **kwargs):
        return render(request,'method.html')


class Job(View):
    def get(self, request, *args, **kwargs):
        return render(request,'job.html')


class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request,'contact.html')
    

class JobApplication(View):
    def get(self, request, *args, **kwargs):
        return render(request,'job-apply.html')
    
    def post(self, request, *args, **kwargs):
        context = request.POST
        return JsonResponse(context)
    
class ProjectPlanner(View):
    def get(self, request, *args, **kwargs):
        return render(request,'project-planner.html')
