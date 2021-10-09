from .serializers import DocumentSerializer
from .models import Document
from .serializers import DocumentRequestSerializer
from .models import DocumentRequest
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class DocumentView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        documents_serializer = DocumentSerializer(data=request.data)
        if documents_serializer.is_valid():
            documents_serializer.save()
            return Response(documents_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', documents_serializer.errors)
            return Response(documents_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
