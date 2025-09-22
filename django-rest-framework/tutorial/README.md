# Project Title: Django Snippet API

## Description
This project is a simple web API for managing code snippets. It allows users to create, retrieve, update, and delete snippets of code, with support for syntax highlighting using Pygments.

## Requirements
- Python 3.x
- Django
- Django REST Framework
- Pygments

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd tutorial
   ```

2. **Create a virtual environment:**
   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install the required packages:**
   ```
   pip install django
   pip install djangorestframework
   pip install pygments
   ```

4. **Run migrations:**
   ```
   python manage.py makemigrations snippets
   python manage.py migrate
   ```

5. **Start the development server:**
   ```
   python manage.py runserver
   ```

6. **Access the API:**
   The API can be accessed at `http://127.0.0.1:8000/snippets/`.

## API Endpoints
- `GET /snippets/` - List all snippets
- `POST /snippets/` - Create a new snippet
- `GET /snippets/<id>/` - Retrieve a specific snippet
- `PUT /snippets/<id>/` - Update a specific snippet
- `DELETE /snippets/<id>/` - Delete a specific snippet

## License
This project is licensed under the MIT License.