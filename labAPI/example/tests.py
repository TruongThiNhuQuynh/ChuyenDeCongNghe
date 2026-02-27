from django.test import TestCase
from django.utils import timezone
from example.models import CustomerReportRecord, ToDoList, ToDoItem, BlogPostItem
from example.serializers import (
    CustomerReportSerializer, ToDoItemSerializer, BlogPostSerializer
)


class ValidatorTests(TestCase):
    def test_unique_validator_on_reference(self):
        CustomerReportRecord.objects.create(reference='REF123', description='A')
        data = {'reference': 'REF123', 'description': 'B'}
        serializer = CustomerReportSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('reference', serializer.errors)

    def test_unique_together_validator(self):
        l = ToDoList.objects.create(name='My List')
        ToDoItem.objects.create(list=l, position=1, title='First')
        data = {'list': l.id, 'position': 1, 'title': 'Duplicate'}
        serializer = ToDoItemSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors)

    def test_unique_for_year_validator(self):
        BlogPostItem.objects.create(slug='post', published=timezone.datetime(2024,1,1).date())
        data = {'slug': 'post', 'published': '2024-05-01'}
        serializer = BlogPostSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('slug', serializer.errors)
