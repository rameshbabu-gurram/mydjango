from django.shortcuts import render

# Create your views here.
from django.views import generic
from . import models

class IndexView(generic.TemplateView):
    template_name = 'regular/index.html'
