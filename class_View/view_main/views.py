from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from view_main import models
from django.urls import reverse_lazy

'''class indexview(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data( **kwargs)
        context['Name']="i am avijit Sarkar"
        return context'''

class list_view(ListView):
    context_object_name='Musician_list'
    model=models.musician
    template_name='index.html'

class Details_view(DetailView):
    context_object_name='Musician_details'
    model=models.musician
    template_name='details.html'

class Addview(CreateView):
    fields=('FirstName','LastName','instument')
    model=models.musician
    template_name='create.html'

class update_view(UpdateView):
    fields=('FirstName','LastName','instument')
    model=models.musician
    template_name='create.html'

class delect_view(DeleteView):
    context_object_name="musician"
    model=models.musician
    success_url=reverse_lazy('index')
    template_name="delect.html"
   

    
