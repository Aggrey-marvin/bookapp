from django.shortcuts import render

# Create your views here.
def index(request):
  
  return render(request, 'base/index.html')

def addSubject(request):
  
  return render(request, 'base/add_subject.html')

def administrator(request):
  
  return render(request, 'base/admin_page.html')

def student(request):
  
  return render(request, 'base/student_page')