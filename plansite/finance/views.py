from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Finance
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    return render(request,'finance/homePage.html')

class FinancesList(ListView):
    model = Finance

def create(request):
    if request.method == "POST":
        finance = Finance()
        finance.title = request.POST.get("title")
        finance.costs = request.POST.get("costs")
        finance.budget = request.POST.get("budget")
        finance.description= request.POST.get("description")
        finance.date= request.POST.get("date")
        finance.type= request.POST.get("type")
        finance.save()
        return HttpResponseRedirect("/finance/table")


