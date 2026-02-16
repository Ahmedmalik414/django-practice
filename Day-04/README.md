# Day 04 — Django Admin

## Goals
- Use Django Admin for real data management
- Make admin usable with filters, search, and clean lists
- Learn how to organize complex models in the admin UI

## What I Practiced
- Registered models in `admin.py`
- Added `list_display`, `list_filter`, and `search_fields`
- Used `prepopulated_fields` for automatic slugs
- Organized fields with `fieldsets`

## Key Concepts
- Admin is for **content management**, not just debugging
- Custom admin config makes data easier to manage
- Good admin setup saves hours later

## Commands Used
```bash
python manage.py createsuperuser
python manage.py runserver
```

## Notes
- Use `list_select_related` for faster admin pages
- Add `date_hierarchy` for time‑based navigation
- Keep admin clean: only show what helps decision‑making

