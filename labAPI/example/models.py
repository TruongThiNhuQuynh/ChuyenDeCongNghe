from django.db import models
from django.utils import timezone

class CustomerReportRecord(models.Model):
    time_raised = models.DateTimeField(default=timezone.now, editable=False)
    reference = models.CharField(unique=True, max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.reference

class ToDoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ToDoItem(models.Model):
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    position = models.IntegerField()
    title = models.CharField(max_length=200)

    class Meta:
        unique_together = (('list', 'position'),)

    def __str__(self):
        return self.title

class BlogPostItem(models.Model):
    slug = models.SlugField()
    published = models.DateField()

    class Meta:
        unique_together = ()

    def __str__(self):
        return self.slug

class BillingRecord(models.Model):
    client = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
