# mysite/mysite/README.md

# Django Project Setup

This is a Django project that includes a simple polls application. Below are the instructions to set up and run the project.

## Project Structure

```
mysite
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── polls
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   └── demo_person.py
├── model_layer
└── README.md
```

## Setup Instructions

1. Navigate to the project directory in the terminal.
2. Ensure that you have Django installed in your Python environment. If not, install it using pip:
   ```
   pip install django
   ```
3. Run the following command to apply migrations:
   ```
   python manage.py migrate
   ```
4. Start the development server with:
   ```
   python manage.py runserver
   ```
5. Access the application in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Running the Demo Script

You can also run the demo script by executing:
```
python polls/demo_person.py
```