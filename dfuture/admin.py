from django.contrib import admin
from .models import Document
from .models import DocumentRequest

# Register your models here.
admin.site.register(Document)
admin.site.register(DocumentRequest)
