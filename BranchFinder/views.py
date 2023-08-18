from django.http import HttpResponse
from django.template import loader
from .models import Branch,LinksMaster
from django.shortcuts import render


def BranchFinder(request):
  mybranchs = Branch.objects.all().values()
  template = loader.get_template('AllBranch.html')
  #template = loader.get_template('RRN.html')
  context = {
    'mybranchs': mybranchs,
  }
  return HttpResponse(template.render(context, request))

def link_list(request):
    links = LinksMaster.objects.all()
    return render(request, 'link_list.html', {'links': links})

def RRN(request):
  return render(request, 'RRN.html')

def Home(request):
  return render(request, 'Error404.html')

def Base(request):
  return render(request, 'base.html')



# Create your views here.
