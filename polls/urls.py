from django.urls import path
from .views import HomeView, DemoFieldsListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('demo/', DemoFieldsListView.as_view(), name='demo_list'),
]