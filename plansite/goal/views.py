from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h3> Hello world! </h3>")
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Goals

class GoalsList(ListView):
    model = Goals