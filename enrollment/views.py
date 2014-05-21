from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from enrollment.models import Student,Course

def StuCreate(request):
      return HttpResponse("Hello world")	
'''
class IndexView(generic.ListView):
    template_name = 'enrollment/index.html'
    context_object_name = 'Course_list'

    def get_queryset(self):
        return Course.objects.all()
'''
