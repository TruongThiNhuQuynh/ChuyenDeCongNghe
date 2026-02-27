from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator, UniqueForYearValidator
from django.utils import timezone
from .models import CustomerReportRecord, ToDoItem, BlogPostItem, BillingRecord


class CustomerReportSerializer(serializers.ModelSerializer):
    reference = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=CustomerReportRecord.objects.all())]
    )

    class Meta:
        model = CustomerReportRecord
        fields = ['id', 'time_raised', 'reference', 'description']


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['id', 'list', 'position', 'title']
        validators = [
            UniqueTogetherValidator(queryset=ToDoItem.objects.all(), fields=['list', 'position'])
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostItem
        fields = ['id', 'slug', 'published']
        validators = [
            UniqueForYearValidator(queryset=BlogPostItem.objects.all(), field='slug', date_field='published')
        ]


# Custom validators
def even_number(value):
    if value % 2 != 0:
        raise serializers.ValidationError('This field must be an even number.')


class MultipleOf:
    requires_context = False

    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if value % self.base != 0:
            raise serializers.ValidationError(f'This field must be a multiple of {self.base}.')


class BillingRecordSerializer(serializers.ModelSerializer):
    # demonstrate disabling default unique validators by not using ModelSerializer defaults for unique_together
    amount = serializers.IntegerField(validators=[even_number, MultipleOf(5)])

    class Meta:
        model = BillingRecord
        fields = ['id', 'client', 'date', 'amount']
        extra_kwargs = {'client': {'required': False}}
        validators = []  # remove default unique together (example of disabling validators)


class OwnerRecordSerializer(serializers.Serializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(default=serializers.CreateOnlyDefault(timezone.now))
    note = serializers.CharField()
