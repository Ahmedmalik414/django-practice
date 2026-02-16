# Day 03 — Models & Database

## Goals
- Understand Django ORM and model design
- Create models and run migrations
- Insert/query data using Django shell
- Render database data in templates

## What I Practiced
- Built a blog data model with relationships
- Ran migrations and verified the schema
- Inserted sample data through `shell`
- Displayed posts with categories and tags

## Key Concepts
- ORM: write queries in Python instead of SQL
- Migrations: track schema changes
- Relationships:
  - `ForeignKey` for one-to-many
  - `ManyToManyField` for tags

## Commands Used
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell
```

## Notes
- Keep model names singular (`Tag`, not `Tags`)
- Use `__str__` for readable admin and shell output
- Migrations should be committed to Git

