from django.contrib import admin
from .models import Question, Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question_text", "pub_date")
    search_fields = ("question_text",)
    list_filter = ("pub_date",)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "choice_text", "votes", "question")
    list_filter = ("question",)
