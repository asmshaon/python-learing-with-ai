"""
Chapter 04: Django Tutorial
=============================

Notes
-----
- Django is a high-level Python web framework.
- Install: pip install django
- Create project: django-admin startproject mysite
- Create app: python manage.py startapp myapp
- Define models in models.py, run migrations to create DB tables.
- Views handle requests; urls.py routes URLs to views.
- Templates (HTML) render the response.
- Run: python manage.py runserver

Run:  python3 chapters/04_libraries/04_django_tutorial.py
"""

# pip install django

# ---------------------------------------------------------------------------
# Problem 1: Show the Django project creation command
#   Input:  None
#   Output: "django-admin startproject mysite"
# ---------------------------------------------------------------------------
def problem_1():
    pass


# ---------------------------------------------------------------------------
# Problem 2: Show the command to create a new app inside a project
#   Input:  None
#   Output: "python manage.py startapp blog"
# ---------------------------------------------------------------------------
def problem_2():
    pass


# ---------------------------------------------------------------------------
# Problem 3: Show the command to run migrations and start the server
#   Input:  None
#   Output: ["python manage.py migrate", "python manage.py runserver"]
# ---------------------------------------------------------------------------
def problem_3():
    pass


if __name__ == "__main__":
    print("Problem 1:", problem_1())
    print("Problem 2:", problem_2())
    print("Problem 3:", problem_3())
