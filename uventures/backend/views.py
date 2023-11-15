from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def works(request):
    return render(request, 'projects.html')
def contact(request):
    return render(request, 'contact.html')
def service(request):
    return render(request, 'service.html')
def blog(request):
    return render(request, 'blog.html')
def team(request):
    return render(request, 'team.html')
def singleteam(request):
    return render(request, 'singleteam.html')


