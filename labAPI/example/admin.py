from django.contrib import admin
from .models import CustomerReportRecord, ToDoList, ToDoItem, BlogPostItem, BillingRecord

admin.site.register(CustomerReportRecord)
admin.site.register(ToDoList)
admin.site.register(ToDoItem)
admin.site.register(BlogPostItem)
admin.site.register(BillingRecord)
