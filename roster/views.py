from django.shortcuts import render
from .models import Paddler
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    paddlers = Paddler.objects.order_by('-last_name')
    template = loader.get_template('roster/index.html')
    context = {
        'paddlers': paddlers,
    }
    return HttpResponse(template.render(context, request))