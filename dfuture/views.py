from .serializers import DocumentSerializer
from .models import Document
from .serializers import DocumentRequestSerializer
from .models import DocumentRequest
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


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
            data = documents_serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            print('error', documents_serializer.errors)
            return Response(documents_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentRequestView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        document_requests = DocumentRequest.objects.all()
        serializer = DocumentRequestSerializer(document_requests, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        document_requests_serializer = DocumentRequestSerializer(data=request.data)
        if document_requests_serializer.is_valid():
            document_requests_serializer.save()
            return Response(document_requests_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', document_requests_serializer.errors)
            return Response(document_requests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, document_req_id, **kwargs):
        try:
            docRequest = DocumentRequest.objects.get(pk=document_req_id)
        except DocumentRequest.DoesNotExist:
            return Response({'error': 'DocumentRequest does not exist'}, status=status.HTTP_404_NOT_FOUND)
        docRequest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)