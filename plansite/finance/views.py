from django.http import HttpResponse
from django.shortcuts import render
from .models import Finance
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    return render(request,'finance/main.html')

class FinancesList(ListView):
    model = Finance