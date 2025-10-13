from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerReportRecord, ToDoItem, BlogPostItem, BillingRecord
from .serializers import (
    CustomerReportSerializer, ToDoItemSerializer, BlogPostSerializer, BillingRecordSerializer, OwnerRecordSerializer
)
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.utils import timezone
import time


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


# --- Caching demo views ---
class CachedPostView(generics.GenericAPIView):
    # Cache page for this GET for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, format=None):
        # include timestamp so caching effect is visible
        content = {
            'title': 'Cached Post',
            'body': 'This content is cached',
            'timestamp': time.time(),
        }
        return Response(content)


class CachedProfileView(generics.GenericAPIView):
    # Cache per-auth header for each user for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers('Authorization'))
    def get(self, request, format=None):
        content = {
            'profile_feed': 'profile data',
            'timestamp': time.time(),
        }
        return Response(content)


@cache_page(60 * 15)
@vary_on_cookie
@api_view(['GET'])
def cached_user_list(request):
    data = {
        'user_feed': 'list data',
        'timestamp': time.time(),
    }
    return Response(data)
