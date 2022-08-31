from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from core.page.models import Page
from django.views.generic import  CreateView, UpdateView,ListView
from django.views.generic.base import TemplateView

def search(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''

    options=Page.objects.filter(
        Q(inicio_name_icontrains=q)|
        Q(importar_name_icontrains=q)|
        Q(list_name_icontrains=q)|
        Q(person_name_icontrains=q)
    )

    context={'options':options}

    return render(request,'index.html', context)
