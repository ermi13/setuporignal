from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import DeveloperForm


# Create your views here.
def Register(request):
   form =DeveloperForm()
   if request.method =='POST':
      print(request.POST)
      pn=request.POST.get('phone_number')
      form = DeveloperForm(request.POST)
      
      
      if form.is_valid():   
         form.save()
         return render(request, 'thanks/thanks.html')
   
            
   context = {'form':form}
   return render(request, 'register/register.html', context)