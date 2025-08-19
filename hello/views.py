from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Question, Choice


# View hiển thị danh sách câu hỏi
class IndexView(generic.ListView):
    template_name = "hello/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Chỉ lấy các câu hỏi đã được publish (pub_date <= hiện tại)
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


# View hiển thị chi tiết câu hỏi
class DetailView(generic.DetailView):
    model = Question
    template_name = "hello/detail.html"
    context_object_name = "question"

    def get_queryset(self):
        # Chỉ hiển thị câu hỏi đã publish
        return Question.objects.filter(pub_date__lte=timezone.now())


# View hiển thị kết quả bình chọn
class ResultsView(generic.DetailView):
    model = Question
    template_name = "hello/results.html"
    context_object_name = "question"


# View xử lý vote
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Hiển thị lại form nếu chưa chọn đáp án
        return render(request, "hello/detail.html", {
            "question": question,
            "error_message": "Bạn chưa chọn lựa chọn nào.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Chuyển hướng sang trang kết quả
        return HttpResponseRedirect(reverse("hello:results", args=(question.id,)))
