# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Person

# def index(request):
#     return HttpResponse("Welcome to the Polls application!")

# def person_list(request):
#     persons = Person.objects.all()
#     return render(request, 'polls/person_list.html', {'persons': persons})

from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from .models_demo import DemoFields
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms.forms import NameForm

class HomeView(TemplateView):
    template_name = "home.html"

class DemoFieldsListView(ListView):
    model = DemoFields
    template_name = "demo_list.html"
    context_object_name = "objects"

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            # Xử lý dữ liệu ở đây nếu cần
            return HttpResponseRedirect("/polls/thanks/")
    else:
        form = NameForm()
    return render(request, "name.html", {"form": form})