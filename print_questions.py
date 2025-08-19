import os
import django
from django.utils import timezone

# Thiết lập môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyDjango.settings')
django.setup()

from hello.models import Question, Choice

# --- CREATE ---
q = Question.objects.create(
    question_text="What's new?",
    pub_date=timezone.now()
)

Choice.objects.create(question=q, choice_text="Great!", votes=0)
Choice.objects.create(question=q, choice_text="So so", votes=0)

# --- READ ---
print("\n📌 Danh sách tất cả câu hỏi:")
for question in Question.objects.all():
    print(f"- {question} (id={question.id})")

print("\n📌 Các lựa chọn của câu hỏi vừa tạo:")
for choice in q.choices.all():
    print(f"  * {choice} (votes={choice.votes})")

# --- UPDATE ---
c = q.choices.first()
c.votes = 5
c.save()
print(f"\n✅ Đã cập nhật votes của '{c.choice_text}' thành {c.votes}")

# --- DELETE ---
to_delete = q.choices.last()
to_delete.delete()
print(f"\n❌ Đã xoá lựa chọn: {to_delete.choice_text}")

# In lại danh sách lựa chọn sau khi xoá
print("\n📌 Các lựa chọn còn lại:")
for choice in q.choices.all():
    print(f"  * {choice} (votes={choice.votes})")
