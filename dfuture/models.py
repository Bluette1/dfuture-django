from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
  return 'uploads/filename'.format(filename=filename)

class DocumentRequest(models.Model):
  name = models.CharField(max_length=20)
  uploaded = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-created_at',]
  
  def __str__(self):
    return self.name
    
class Document(models.Model):
  name = models.CharField(max_length=20)
  client_name = models.CharField(max_length=20)
  uploaded_at = models.DateTimeField(auto_now_add=True)
  file = models.FileField(_("File"), upload_to=upload_to)
    
  def __str__(self):
      return self.name
