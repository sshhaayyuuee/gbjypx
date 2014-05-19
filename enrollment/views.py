from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from enrollment.models import Student,Course

class IndexView(generic.ListView):
    template_name = 'enrollment/index.html'
    context_object_name = 'Course_list'

    def get_queryset(self):
        return Course.objects.all()
	
class DetailView(generic.DetailView):
    model = Student
    template_name = 'enrollment/detail.html'
	
class StuCreate(CreateView):
    model = Student
    context_object_name = 'course_id'
    fields = ['name','nation','dept','position','cellphone','workphone','course']
    template_name = 'enrollment/stucreate.html'
	
	
class StuUpdate(UpdateView):
    model = Student
    fields = ['name']
	
class AuthorDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('Stu-list')
	
def stu(request,number):
    
    return render_to_response('stucreate.html')
