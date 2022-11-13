from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.SubjectView.as_view(), name='subjects'),
    path('addSubject/', views.CreateSubjectView.as_view(), name='addSubject'),
    path('subjects/<int:pk>/update', views.UpdateSubjectView.as_view(), name='subjectUpdate'),
    path('subjects/<int:pk>/delete', views.DeleteSubjectView.as_view(), name='subjectDelete'),
    path('administrator/', views.administrator, name='administrator'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
]
