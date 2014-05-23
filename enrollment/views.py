from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse

# Create your views here.
from enrollment.models import StudentForm, Course

def StuCreate(request, course_id):
    if request.method == 'POST': # If the form has been submitted...
        # StudentForm was defined in the previous section
        form = StudentForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            new_data = form.save(commit=False)
            new_data.course = Course.objects.get(pk=course_id)
            new_data.save()
            return HttpResponseRedirect('/enrollment/thanks/') # Redirect after POST
    else:
        form = StudentForm()  # An unbound form

    return render(request, 'enrollment/stucreate.html', {
        'form': form,
        'course_id': course_id,
    })

class IndexView(generic.ListView):
    template_name = 'enrollment/index.html'
    context_object_name = 'Course_list'

    def get_queryset(self):
        return Course.objects.all()

def thanks(request):
    return HttpResponse('谢谢报名')

