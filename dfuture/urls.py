from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.DocumentView.as_view(), name= 'documents_list'),
    path('document_requests/', views.DocumentRequestView.as_view(), name= 'document_requests_list'),
    path('document_requests/<int:document_req_id>', views.DocumentRequestView.as_view(), name= 'document_requests_list'),
]