from django.db import models

class DocumentRequest(models.Model):
    name = models.CharField(max_length=20)
    uploaded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Meta:
  order = ['-created_at',]