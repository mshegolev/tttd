from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Finance


# Create your views here.
def index(request):
    return render(request, 'finance/homePage.html')


def create(request):
    if request.method == "POST":
        finance = Finance()
        finance.title = request.POST.get("title")
        finance.costs = request.POST.get("costs")
        finance.budget = request.POST.get("budget")
        finance.description = request.POST.get("description")
        finance.date = request.POST.get("date")
        finance.type = request.POST.get("type")
        finance.save()
        return HttpResponseRedirect("/finance/table")


class FinanceList(ListView):
    model = Finance


class FinanceView(DetailView):
    model = Finance


class FinanceCreate(CreateView):
    model = Finance
    fields = ['title', 'costs','budget', 'description', 'date', 'type']
    success_url = reverse_lazy('finance_list')


class FinanceUpdate(UpdateView):
    model = Finance
    fields = ['title', 'costs', 'budget', 'description', 'date', 'type']
    success_url = reverse_lazy('finance_list')


class FinanceDelete(DeleteView):
    model = Finance
    success_url = reverse_lazy('finance_list')
