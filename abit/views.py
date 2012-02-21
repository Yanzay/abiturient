﻿# coding=utf-8
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render_to_response, redirect
from django.views.generic.list import ListView
from abit.forms import AbitRequestForm
from abit.models import AbitRequest, EducationalForm
from abit.dummy import Generator

class AddAbitRequestView(CreateView):
    model = AbitRequest
    template_name = 'abitrequest_form.html'
    context_object_name = 'abit_form'
    form_class = AbitRequestForm
    success_url = '/abit/list/'

    def form_valid(self, form):
        inst = form.save(commit=False)
        inst.creator = self.request.user
        inst.save()
        return redirect(self.success_url)

class AbitRequestListView(ListView):
#    model = AbitRequest
    template_name = 'reqslist.html'
    context_object_name = 'abitrequest_list'
    paginate_by = 50

    def get_queryset(self):
        return AbitRequest.objects.all().order_by('-date')

class EditAbitRequestView(UpdateView):
    model = AbitRequest
    template_name = 'abitrequest_form.html'
    context_object_name = 'abit_form'
    form_class = AbitRequestForm

def Init(request):
    g = Generator()
    g.generateBase()
    g.generateAbitRequests(request)
    return HttpResponseRedirect('/abit/list/')
