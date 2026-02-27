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

Caching demo
------------

The project includes endpoints that demonstrate Django's caching decorators used with DRF views.

Endpoints:

- GET /api/cached/post/     — class-based view with @cache_page; response includes `timestamp` so you can see caching in action.
- GET /api/cached/profile/  — class-based view cached and varied on `Authorization` header.
- GET /api/cached/users/    — function-based view (uses `@api_view`) cached and varied on cookie.

Quick test steps (cmd.exe):

1. Start the server

    .venv\Scripts\python.exe manage.py runserver

2. Call the same endpoint twice (timestamp shows caching)

    curl http://127.0.0.1:8000/api/cached/post/
    curl http://127.0.0.1:8000/api/cached/post/

The two responses should show the same `timestamp` if the first response was cached.

To test vary_on_headers (profile): send with and without an Authorization header and compare timestamps:

    curl http://127.0.0.1:8000/api/cached/profile/
    curl -H "Authorization: Token abc" http://127.0.0.1:8000/api/cached/profile/

To test vary_on_cookie (users): the cached response is per cookie; you can use curl's `-b` and `-c` to set cookiejar, or test in browser.

Filtering demo
--------------

The project includes several views demonstrating different filtering strategies:

- GET /api/filter/by-user/         — example get_queryset() filtered by request.user (requires authentication to return items in demo)
- GET /api/filter/by-url/<username>/ — example filtering using a URL path parameter
- GET /api/filter/by-query/?list_name=Name — example filtering using query parameters
- GET /api/filter/django-filter/?position=1&search=term&ordering=-position — example using DjangoFilterBackend + SearchFilter + OrderingFilter

Test examples (cmd.exe):

# Filter by query param (list_name)
curl "http://127.0.0.1:8000/api/filter/by-query/?list_name=My%20List"

# Filter by URL
curl http://127.0.0.1:8000/api/filter/by-url/My%20List/

# DjangoFilterBackend example: filter, search and ordering
curl "http://127.0.0.1:8000/api/filter/django-filter/?position=1&search=task&ordering=-position"

Note: for the `by-user` example, log in via the browsable API or use session/cookie auth to see results. The demo `get_queryset()` implementations are simple and intended to show filtering patterns — adapt them for your real models and user relations.

Pagination demo
---------------

This project includes two example pagination endpoints:

- GET /api/paginate/page/        — PageNumberPagination (default page param `?page=2`) using `StandardResultsSetPagination`.
- GET /api/paginate/limitoffset/ — LimitOffsetPagination using `StandardLimitOffsetPagination` (params `?limit=5&offset=10`).

These endpoints use the `ToDoItem` queryset and are ready to be tested once you have multiple items in the database.

Quick test (cmd.exe) — create several items first (or use admin) then:

# PageNumber pagination
curl "http://127.0.0.1:8000/api/paginate/page/?page=1"
curl "http://127.0.0.1:8000/api/paginate/page/?page=2"

# LimitOffset pagination
curl "http://127.0.0.1:8000/api/paginate/limitoffset/?limit=1&offset=0"
curl "http://127.0.0.1:8000/api/paginate/limitoffset/?limit=1&offset=1"

Typical PageNumber response structure:
{
    "count": 42,
    "next": "http://127.0.0.1:8000/api/paginate/page/?page=2",
    "previous": null,
    "results": [ ... ]
}

Typical LimitOffset response structure matches the REST framework style and contains `count`, `next`, `previous`, and `results`.

