from django.db import models

# Create your models here.
class Subject(models.Model):
  subjectName = models.CharField(max_length=256)
  
class Book(models.Model):
  bookName = models.CharField(max_length=256)
  author = models.CharField(max_length = 256)
  isbn = models.CharField(max_length = 256)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  published = models.DateField()