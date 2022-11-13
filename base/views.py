from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View

from .models import Subject

# Create your views here.
def index(request):
  
  return render(request, 'base/index.html')

class SubjectView(View):
  def get(self, request):
    subjects = Subject.objects.all()
    
    context = {
      'subjects': subjects,
    }
    
    return render(request, 'base/subject.html', context)

class CreateSubjectView(CreateView):
  model = Subject
  fields = '__all__'
  template_name = 'base/add_subject.html'
  success_url = reverse_lazy('base:subjects')
  
class UpdateSubjectView(UpdateView):
  model = Subject
  fields = '__all__'
  template_name = 'base/update_subject.html'
  success_url = reverse_lazy('base:subjects')
  
class DeleteSubjectView(DeleteView):
  model = Subject
  template_name = 'base/delete_subject.html'
  success_url = reverse_lazy('base:subjects')

def administrator(request):
  
  return render(request, 'base/admin_page.html')

def student(request):
  
  return render(request, 'base/student_page.html')

def teacher(request):
  
  return render(request, "base/teacher_page.html")