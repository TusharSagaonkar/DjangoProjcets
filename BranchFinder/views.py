from django.http import HttpResponse
from django.template import loader
from .models import Branch



def BranchFinder(request):
  mybranchs = Branch.objects.all().values()
  template = loader.get_template('AllBranch.html')
  context = {
    'mybranchs': mybranchs,
  }
  return HttpResponse(template.render(context, request))

# Create your views here.
