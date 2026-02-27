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
from rest_framework import generics
from .models import ToDoItem, ToDoList
from .serializers import ToDoItemSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import StandardResultsSetPagination, StandardLimitOffsetPagination


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


# --- Filtering demo views ---
class PurchaseListByUser(generics.ListAPIView):
    """Filter queryset against request.user (example uses ToDoItem)."""
    serializer_class = ToDoItemSerializer

    def get_queryset(self):
        user = self.request.user
        # For demo: return items belonging to the first ToDoList if authenticated, else none
        if user and user.is_authenticated:
            # this is just a demo — normally you'd filter by a user foreign key
            lists = ToDoList.objects.all()
            if lists.exists():
                return ToDoItem.objects.filter(list=lists.first())
        return ToDoItem.objects.none()


class PurchaseListByURL(generics.ListAPIView):
    serializer_class = ToDoItemSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        # demo: filter by ToDoList name matching username
        return ToDoItem.objects.filter(list__name=username)


class PurchaseListByQueryParam(generics.ListAPIView):
    serializer_class = ToDoItemSerializer

    def get_queryset(self):
        queryset = ToDoItem.objects.all()
        list_name = self.request.query_params.get('list_name')
        if list_name is not None:
            queryset = queryset.filter(list__name=list_name)
        return queryset


class ProductListWithDjangoFilter(generics.ListAPIView):
    """Example showing DjangoFilterBackend with filterset_fields."""
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['position', 'title']
    search_fields = ['title']
    ordering_fields = ['position', 'id']


class PaginatedToDoListPageNumber(generics.ListAPIView):
    """Demonstrate PageNumberPagination using StandardResultsSetPagination"""
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    pagination_class = StandardResultsSetPagination


class PaginatedToDoListLimitOffset(generics.ListAPIView):
    """Demonstrate LimitOffsetPagination using StandardLimitOffsetPagination"""
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    pagination_class = StandardLimitOffsetPagination
