from django.urls import path
from . import views

urlpatterns = [
    path('customer_reports/', views.CustomerReportCreate.as_view(), name='customer-report-create'),
    path('todo_items/', views.ToDoItemCreate.as_view(), name='todoitem-create'),
    path('blog_posts/', views.BlogPostCreate.as_view(), name='blogpost-create'),
    path('billing/', views.BillingRecordCreate.as_view(), name='billing-create'),
    path('owner_example/', views.OwnerRecordExample.as_view(), name='owner-example'),
    # caching demo
    path('cached/post/', views.CachedPostView.as_view(), name='cached-post'),
    path('cached/profile/', views.CachedProfileView.as_view(), name='cached-profile'),
    path('cached/users/', views.cached_user_list, name='cached-user-list'),
]
