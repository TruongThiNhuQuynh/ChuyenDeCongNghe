import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


def create_question(question_text, days):
    """
    Tạo một câu hỏi với pub_date lệch so với hiện tại 'days'.
    days > 0  => tương lai
    days < 0  => quá khứ
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        future_question = create_question("future", days=30)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        old_question = create_question("old", days=-2)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        # trong vòng 1 ngày
        recent_question = create_question("recent", days=0)
        recent_question.pub_date = timezone.now() - datetime.timedelta(hours=1)
        recent_question.save()
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        url = reverse("hello:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertEqual(list(response.context["latest_question_list"]), [])

    def test_past_question(self):
        q = create_question("past question", days=-30)
        url = reverse("hello:index")
        response = self.client.get(url)
        self.assertEqual(list(response.context["latest_question_list"]), [q])

    def test_future_question(self):
        create_question("future question", days=30)
        url = reverse("hello:index")
        response = self.client.get(url)
        self.assertContains(response, "No polls are available.")
        self.assertEqual(list(response.context["latest_question_list"]), [])

    def test_future_and_past_questions(self):
        past_q = create_question("past q", days=-30)
        create_question("future q", days=30)
        url = reverse("hello:index")
        response = self.client.get(url)
        self.assertEqual(list(response.context["latest_question_list"]), [past_q])

    def test_two_past_questions(self):
        older_q = create_question("older past", days=-30)
        newer_q = create_question("newer past", days=-5)
        url = reverse("hello:index")
        response = self.client.get(url)
        # phải sắp xếp mới nhất trước
        self.assertEqual(
            list(response.context["latest_question_list"]),
            [newer_q, older_q],
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_q = create_question("future", days=5)
        url = reverse("hello:detail", args=(future_q.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_q = create_question("past", days=-5)
        url = reverse("hello:detail", args=(past_q.id,))
        response = self.client.get(url)
        self.assertContains(response, past_q.question_text)
