from django.urls import path
from django.views.generic import ListView, DetailView

from goal.models import Goals

urlpatterns = [  # path('', views.index, name='index'),
    path('', ListView.as_view(queryset=Goals.objects.all().order_by("-date")[:20], template_name="goal/goals.html")),
    path('<int:pk>', DetailView.as_view(model=Goals, template_name='goal/goal.html')),

]
