from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('addSubject/', views.addSubject, name='addSubject'),
    path('administrator/', views.administrator, name='administrator'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
]
