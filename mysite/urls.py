from django.contrib import admin
from django.urls import path, include
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  # Assuming you will create a urls.py in the polls app
]