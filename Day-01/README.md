# Day 01 — Django Fundamentals + Environment Setup

## Goals
- Understand how Django works at a high level
- Learn the project/app structure
- Run the development server confidently

## What I Practiced
- Created a Django project and first app
- Explored `settings.py`, `urls.py`, and `views.py`
- Ran the development server and verified routes

## Key Concepts
- MVT architecture (Model–View–Template)
- Project vs App separation
- Virtual environments for dependency isolation

## Commands Used
```bash
python -m venv venv
python manage.py startproject day01pro
python manage.py startapp app1
python manage.py runserver
```

## Notes
- Keep the virtual environment isolated per project
- The `urls.py` file is the traffic controller

