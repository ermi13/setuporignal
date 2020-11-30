from django.shortcuts import render

# Create your views here.
from home.models import Plan
from .models import Discount
def price(request, name):
    plan = Plan.objects.filter(service__name= name)
    discount = Discount.objects.all()
    uptoo = ''
    for d in discount:
       uptoo = d.upto
    return render(request, 'price/price.html',{'name' :name, 'plans':plan , 'discount': discount , 'upto':uptoo })
