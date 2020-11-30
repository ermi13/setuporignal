from django.shortcuts import render

from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
from .models import Service

def home(request):
    services = Service.objects.all().order_by('order')

    return render(request, 'home/home.html',{'services' :services })

def feedback(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    comment = request.POST.get('comment')

    send_mail("%s 's feedback to Setup systems" % (name),
              comment,
              email,
              ['ermiyeasti22@gmail.com'],
              fail_silently=False)


    services = Service.objects.all()
    sent=True
    return render(request, 'home/home.html',{'services' :services,'sent':sent,'name':name })


