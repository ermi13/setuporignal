from django.shortcuts import render

# Create your views here.
def Portfolios(request):
     return render(request, 'portfolios/portfolios.html')
