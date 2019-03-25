"""plansite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.views.generic import ListView, DetailView, UpdateView
from .models import Finance
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('table', ListView.as_view(queryset=Finance.objects.all().order_by("-date")[:20],
                                   template_name="finance/table.html")),
    path('addFinance', ListView.as_view(queryset=Finance.objects.all().order_by("-date")[:20],
                                        template_name="finance/addFinance.html")),
    path('create/', views.create),


    path('finance_list', views.FinanceList.as_view(), name='finance_list'),
    path('view/<int:pk>', views.FinanceView.as_view(), name='finance_view'),
    path('new', views.FinanceCreate.as_view(), name='finance_new'),
    path('view/<int:pk>', views.FinanceView.as_view(), name='finance_view'),
    path('edit/<int:pk>', views.FinanceUpdate.as_view(), name='finance_edit'),
    path('delete/<int:pk>', views.FinanceDelete.as_view(), name='finance_delete'),

]
