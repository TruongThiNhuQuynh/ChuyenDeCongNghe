from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def index(request):
    return HttpResponse("Welcome to the Polls application!")

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'polls/person_list.html', {'persons': persons})