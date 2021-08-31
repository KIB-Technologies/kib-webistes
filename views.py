from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import *

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')
    
def products(request):
    return render(request, 'products.html')

#it_services
def it_services(request):
    return render(request, 'it_services.html')

def web_development(request):
    return render(request, 'web_development.html')

def mobile_app_development(request):
    return render(request, 'mobile_app_development.html')

def software_development(request):
    return render(request, 'software_development.html')

def game_development(request):
    return render(request, 'game_development.html')

def cyber_security(request):
    return render(request, 'cyber_security.html')

def graphic_designing(request):
    return render(request, 'graphic_designing.html')

#marketing Services
#it_services
def marketing_services(request):
    return render(request, 'marketing_services.html')

def multimedia_marketing(request):
    return render(request, 'multimedia_marketing.html')

def cinema_branding(request):
    return render(request, 'cinema_branding.html')

def event_managment(request):
    return render(request, 'event_managment.html')

def digital_marketing(request):
    return render(request, 'digital_marketing.html')

def out_of_home_ads(request):
    return render(request, 'out_of_home_ads.html')


def blog(request):
    Blogs = Blog.objects.all()
    return render(request, 'blog.html', {'Blogs': Blogs})

def blogfull(request, bid):
    blog = Blog.objects.get(id=bid)
    return render(request, 'blogfull.html', {'Blog': blog})

def career(request):
    return render(request,'career.html')
    
def privacypolicy(request):
    return render(request,'privacy.html')

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()
        subject = 'Query From : '+ str(contact.name)+' From KIB Website'
        message = 'Query From : '+ str(contact.name)+' Query Email : '+ str(contact.email)+' Query Subject : '+ str(contact.subject)+ ' Query: '+ str(contact.message)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['info.kibtech@gmail.com','sumit@kibtechnologies.com','ayushtyagi@kibtechnologies.com',]
        send_mail( subject, message, email_from, recipient_list )
        subject = 'Hello '+ str(contact.name)
        message = 'Welcome to KIB Technologies '+ str(contact.name)+' .Thank you for contacting us. We will respond to you soon. For any further queries please contact again anytime.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [contact.email,]
        send_mail( subject, message, email_from, recipient_list )
        messages.success(request,"Query Sent Successfully")
        return redirect('index')
    else:
        return render(request,'contact.html')
   
def returnpolicy(request):
    return render(request,'return.html')
    
def login(request):
    return render(request, 'login.html')
