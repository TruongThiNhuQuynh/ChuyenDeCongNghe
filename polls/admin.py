# from django.contrib import admin
# from .models import Person

# admin.site.register(Person)
from django.contrib import admin
from .models_demo import DemoFields

admin.site.register(DemoFields)