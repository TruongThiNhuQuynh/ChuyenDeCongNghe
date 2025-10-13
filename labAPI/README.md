Django REST Framework Validators - Example Project

This minimal project demonstrates various DRF validators: UniqueValidator, UniqueTogetherValidator, UniqueForYearValidator, HiddenField defaults, CreateOnlyDefault, and custom validators.

Run steps on Windows (cmd.exe):

1. Create and activate virtualenv

    python -m venv .venv
    .venv\Scripts\activate

2. Install requirements

    pip install -r requirements.txt

3. Run migrations

    python manage.py migrate

4. Create a superuser (for admin)

    python manage.py createsuperuser

5. Run the development server

    python manage.py runserver

6. Use the admin at http://127.0.0.1:8000/admin to create initial objects.

7. Example requests (use a tool like curl or Postman). In cmd.exe, using curl shipped with Windows 10+:

# UniqueValidator example (create a CustomerReport with reference REF1 then try to create again to see validation error)
curl -X POST http://127.0.0.1:8000/api/customer_reports/ -H "Content-Type: application/json" -d "{\"reference\": \"REF1\", \"description\": \"First\"}"
curl -X POST http://127.0.0.1:8000/api/customer_reports/ -H "Content-Type: application/json" -d "{\"reference\": \"REF1\", \"description\": \"Second\"}"

# UniqueTogetherValidator example (create two ToDoItems with same list and position)
curl -X POST http://127.0.0.1:8000/api/todo_items/ -H "Content-Type: application/json" -d "{\"list\": 1, \"position\": 1, \"title\": \"A\"}"
curl -X POST http://127.0.0.1:8000/api/todo_items/ -H "Content-Type: application/json" -d "{\"list\": 1, \"position\": 1, \"title\": \"B\"}"

# UniqueForYearValidator example
curl -X POST http://127.0.0.1:8000/api/blog_posts/ -H "Content-Type: application/json" -d "{\"slug\": \"post\", \"published\": \"2024-01-01\"}"
curl -X POST http://127.0.0.1:8000/api/blog_posts/ -H "Content-Type: application/json" -d "{\"slug\": \"post\", \"published\": \"2024-05-01\"}"

# Custom validator example (amount must be even and a multiple of 5)
curl -X POST http://127.0.0.1:8000/api/billing/ -H "Content-Type: application/json" -d "{\"client\": \"C1\", \"date\": \"2024-01-01\", \"amount\": 7}"
curl -X POST http://127.0.0.1:8000/api/billing/ -H "Content-Type: application/json" -d "{\"client\": \"C1\", \"date\": \"2024-01-01\", \"amount\": 10}"

Notes for screenshots:
- After running a failed request you will see JSON errors. Take screenshots of these responses as evidence for the pull request.
- Use admin to create a ToDoList with id=1 before hitting the ToDoItem endpoints.
