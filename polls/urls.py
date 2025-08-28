from django.urls import path
from .views import HomeView, DemoFieldsListView, get_name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('demo/', DemoFieldsListView.as_view(), name='demo_list'),
    path('forms/', get_name, name='get_name'),
]