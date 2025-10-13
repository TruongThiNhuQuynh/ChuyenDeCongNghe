from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerReportRecord, ToDoItem, BlogPostItem, BillingRecord
from .serializers import (
    CustomerReportSerializer, ToDoItemSerializer, BlogPostSerializer, BillingRecordSerializer, OwnerRecordSerializer
)


class CustomerReportCreate(generics.CreateAPIView):
    queryset = CustomerReportRecord.objects.all()
    serializer_class = CustomerReportSerializer


class ToDoItemCreate(generics.CreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


class BlogPostCreate(generics.CreateAPIView):
    queryset = BlogPostItem.objects.all()
    serializer_class = BlogPostSerializer


class BillingRecordCreate(generics.CreateAPIView):
    queryset = BillingRecord.objects.all()
    serializer_class = BillingRecordSerializer


class OwnerRecordExample(generics.GenericAPIView):
    serializer_class = OwnerRecordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
